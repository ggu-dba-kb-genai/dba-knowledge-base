#!/usr/bin/env python3
"""Voice audition: render the SAME 8-scene transcript in 6 variants so the user can
pick the best / closest-to-his-accent take.

Hub & spoke — one knob changed per variant off the deployed hub:
  v1 hub  : MTLv3 · natural      · cfg0.5   (deployed baseline)
  v2      : MTLv3 · natural      · cfg0.3   (accent axis, lower)
  v3      : MTLv3 · natural      · cfg0.7   (accent axis, higher)
  v4      : MTLv3 · storytelling · cfg0.5   (style axis)
  v5      : MTLv3 · excited      · cfg0.5   (style axis)
  v6      : English· natural     · cfg0.5   (model contrast)

Each variant: per-scene s1..s8.wav (FROZEN — the take picked is the take that ships),
durations.json, timing.txt (composition block), and a concatenated ~70s preview.
Runaway guard reused from gen_scenes_v2.py.
"""
import os, gc, json, math, subprocess
import torch, torchaudio as ta

REFS = "/home/sanjayg4/chatterbox/refs"
BASE = "/mnt/c/Users/csp/Downloads/my-voice-recording/voice-options"
PREV = os.path.join(BASE, "previews")
os.makedirs(PREV, exist_ok=True)
EXAG = 0.5
GAP = 0.4  # silence between scenes in the preview

# exact transcript that will ship — identical to gen_scenes_v2.py
SCENES = {
    "s1": "Hello, my fellow DBA cohort members. Welcome to our knowledge base, built entirely from your contributions, and yours alone.",
    "s2": "This is an open, living map of our doctorate in Emerging Technologies, Generative A I, and Artificial Intelligence.",
    "s3": "Six doctoral courses, woven together. From emerging digital technologies and machine learning, to deep learning, generative A I, project design, and responsible A I.",
    "s4": "Inside, you'll find seventy-four sessions, twenty-three core concepts, and over eleven hundred connections linking every idea to the next.",
    "s5": "Everything lives in the Open Knowledge Format. Not buried in slides, but a navigable graph you can explore, search, and build upon.",
    "s6": "Start anywhere. Follow a course, trace a concept, or simply ask, and get answers in plain language.",
    "s7": "And it grows with us. Every note you add makes it richer for everyone.",
    "s8": "Thank you for being part of this. Let's explore what we've built, together.",
}
ORDER = [f"s{i}" for i in range(1, 9)]

# (folder, model, ref, cfg)  — model: "mtl" or "eng"
VARIANTS = [
    ("v1_hub_MTLv3_natural_cfg0.5", "mtl", "natural",      0.5),
    ("v2_natural_cfg0.3",           "mtl", "natural",      0.3),
    ("v3_natural_cfg0.7",           "mtl", "natural",      0.7),
    ("v4_storytelling_cfg0.5",      "mtl", "storytelling", 0.5),
    ("v5_excited_cfg0.5",           "mtl", "excited",      0.5),
    ("v6_ENG_natural_cfg0.5",       "eng", "natural",      0.5),
]


def probe(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path]).decode().strip())


def gen_scene(model, kind, text, ref, cfg):
    """Generate one scene with the duration-band runaway guard. Returns (wav, dur)."""
    words = len(text.split())
    lo, hi = words * 0.28, words * 0.62 + 2.5
    best = None
    for _ in range(6):
        if kind == "mtl":
            wav = model.generate(text, language_id="en", audio_prompt_path=ref,
                                 exaggeration=EXAG, cfg_weight=cfg)
        else:
            wav = model.generate(text, audio_prompt_path=ref,
                                 exaggeration=EXAG, cfg_weight=cfg)
        d = wav.shape[-1] / model.sr
        if best is None or d < best[1]:
            best = (wav, d)
        if lo <= d <= hi:
            best = (wav, d)
            break
    return best


def write_timing(folder, durations):
    LEAD, TAIL = 0.5, 0.8
    start = 0.0
    audio_lines, scene_lines, starts = [], [], {}
    for i, sid in enumerate(ORDER, 1):
        vo = durations[sid]
        sd = vo + LEAD + TAIL
        starts[sid] = start
        audio_lines.append(
            f'      <audio id="a{i}" data-start="{start+LEAD:.2f}" data-duration="{vo:.2f}" '
            f'data-track-index="9" src="audio/{sid}.wav" data-volume="1"></audio>')
        scene_lines.append(f"        {{id:'#sc{i}', s:{start:.2f}, d:{sd:.2f}}}")
        start += sd
    total = math.ceil(start)
    out = []
    out.append("===AUDIO===")
    out += audio_lines
    out.append("\n===SCENES===")
    out.append(",\n".join(scene_lines))
    out.append(f"\n===TOTAL=== {total}")
    out.append(f"counter base (stat scene = sc4 start): {starts['s4']:.2f}")
    out.append(f"TOTAL speech {sum(durations.values()):.1f}s")
    with open(os.path.join(folder, "timing.txt"), "w") as f:
        f.write("\n".join(out) + "\n")


def make_preview(folder, sr, preview_path):
    """Concat s1..s8 with GAP silence between, re-encode to pcm_s16le mono."""
    sil = os.path.join(folder, "_sil.wav")
    subprocess.check_call(["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
                           "-i", f"anullsrc=r={sr}:cl=mono", "-t", str(GAP), sil])
    listf = os.path.join(folder, "_list.txt")
    with open(listf, "w") as f:
        for i, sid in enumerate(ORDER):
            f.write(f"file '{os.path.join(folder, sid + '.wav')}'\n")
            if i != len(ORDER) - 1:
                f.write(f"file '{sil}'\n")
    subprocess.check_call(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                           "-i", listf, "-ar", str(sr), "-ac", "1",
                           "-c:a", "pcm_s16le", preview_path])
    os.remove(sil); os.remove(listf)


def run_variant(model, kind, folder, ref_name, cfg):
    fdir = os.path.join(BASE, folder)
    os.makedirs(fdir, exist_ok=True)
    ref = os.path.join(REFS, f"{ref_name}.wav")
    durations = {}
    for sid in ORDER:
        wav, _ = gen_scene(model, kind, SCENES[sid], ref, cfg)
        path = os.path.join(fdir, f"{sid}.wav")
        ta.save(path, wav, model.sr)
        durations[sid] = round(probe(path), 2)
        print(f"  {folder}/{sid}: {durations[sid]:.2f}s", flush=True)
    with open(os.path.join(fdir, "durations.json"), "w") as f:
        json.dump(durations, f, indent=2)
    write_timing(fdir, durations)
    make_preview(fdir, model.sr, os.path.join(PREV, f"{folder}.wav"))
    print(f"  {folder}: preview written, total speech {sum(durations.values()):.1f}s", flush=True)


def main():
    from chatterbox.mtl_tts import ChatterboxMultilingualTTS
    print("Loading Multilingual V3...", flush=True)
    mtl = ChatterboxMultilingualTTS.from_pretrained(device="cuda", t3_model="v3")
    for folder, kind, ref, cfg in VARIANTS:
        if kind != "mtl":
            continue
        print(f"== {folder} ==", flush=True)
        run_variant(mtl, "mtl", folder, ref, cfg)
    del mtl; gc.collect(); torch.cuda.empty_cache()

    from chatterbox.tts import ChatterboxTTS
    print("Loading English model...", flush=True)
    eng = ChatterboxTTS.from_pretrained(device="cuda")
    for folder, kind, ref, cfg in VARIANTS:
        if kind != "eng":
            continue
        print(f"== {folder} ==", flush=True)
        run_variant(eng, "eng", folder, ref, cfg)

    # README map
    with open(os.path.join(BASE, "README.txt"), "w") as f:
        f.write("Voice audition — same transcript, 6 variants.\n")
        f.write("Listen to previews/<folder>.wav (full ~70s narration each), pick one.\n\n")
        f.write("Accent lever = cfg + model. Style/energy = reference clip (all refs = your voice = same accent).\n\n")
        rows = [
            ("v1_hub_MTLv3_natural_cfg0.5", "MTLv3",   "natural",      "0.5", "deployed baseline (hub)"),
            ("v2_natural_cfg0.3",           "MTLv3",   "natural",      "0.3", "accent: lower cfg"),
            ("v3_natural_cfg0.7",           "MTLv3",   "natural",      "0.7", "accent: higher cfg"),
            ("v4_storytelling_cfg0.5",      "MTLv3",   "storytelling", "0.5", "style"),
            ("v5_excited_cfg0.5",           "MTLv3",   "excited",      "0.5", "style (you liked excited)"),
            ("v6_ENG_natural_cfg0.5",       "English", "natural",      "0.5", "model contrast"),
        ]
        for folder, m, r, c, note in rows:
            f.write(f"{folder:32s} model={m:8s} ref={r:13s} cfg={c}  -> {note}\n")
    print(f"\nALL DONE -> {BASE}", flush=True)


if __name__ == "__main__":
    main()
