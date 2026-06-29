#!/usr/bin/env python3
"""Regenerate all 8 scene voiceovers with the chosen config:
Multilingual V3 model + 'natural' reference + cfg_weight 0.5, language_id 'en'.
Runaway guard: re-roll a scene if its duration falls outside an expected band.
Also computes + prints the exact composition timing block."""
import os, subprocess, json, math
import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

REF = "/home/sanjayg4/chatterbox/refs/natural.wav"
OUT = "/home/sanjayg4/dba-knowledge-base/video-src/audio"
os.makedirs(OUT, exist_ok=True)

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

def probe(path):
    return float(subprocess.check_output(
        ["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",path]).decode().strip())

print("Loading Multilingual V3...", flush=True)
model = ChatterboxMultilingualTTS.from_pretrained(device="cuda", t3_model="v3")

durations = {}
for sid, text in SCENES.items():
    words = len(text.split())
    lo, hi = words * 0.28, words * 0.62 + 2.5   # acceptable seconds band
    best = None
    for attempt in range(1, 7):
        wav = model.generate(text, language_id="en", audio_prompt_path=REF,
                             exaggeration=0.5, cfg_weight=0.5)
        d = wav.shape[-1] / model.sr
        if best is None or d < best[1]:
            best = (wav, d)
        if lo <= d <= hi:
            best = (wav, d)
            break
    path = os.path.join(OUT, f"{sid}.wav")
    ta.save(path, best[0], model.sr)
    durations[sid] = round(probe(path), 2)
    print(f"{sid}: {durations[sid]:.2f}s (band {lo:.1f}-{hi:.1f})", flush=True)

with open(os.path.join(OUT, "durations.json"), "w") as f:
    json.dump(durations, f, indent=2)

# ---- compute composition timing ----
LEAD, TAIL = 0.5, 0.8
order = [f"s{i}" for i in range(1, 9)]
start = 0.0
audio_lines, scene_lines = [], []
for i, sid in enumerate(order, 1):
    vo = durations[sid]
    sd = vo + LEAD + TAIL
    audio_lines.append(
        f'      <audio id="a{i}" data-start="{start+LEAD:.2f}" data-duration="{vo:.2f}" '
        f'data-track-index="9" src="audio/{sid}.wav" data-volume="1"></audio>')
    scene_lines.append(f"        {{id:'#sc{i}', s:{start:.2f}, d:{sd:.2f}}}")
    start += sd
total = math.ceil(start)

print("\n===AUDIO===", flush=True)
print("\n".join(audio_lines), flush=True)
print("\n===SCENES===", flush=True)
print(",\n".join(scene_lines), flush=True)
print(f"\n===TOTAL=== {total}", flush=True)
print(f"TOTAL speech {sum(durations.values()):.1f}s", flush=True)
