#!/usr/bin/env python3
"""Generate per-scene voiceover clips for the KB explainer (storytelling voice).
Outputs audio/s1.wav .. s8.wav and prints each clip's exact duration."""
import os, time, subprocess, json
import torch, torchaudio as ta
from chatterbox.tts import ChatterboxTTS

REF = "/home/sanjayg4/chatterbox/refs/storytelling.wav"
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

print("Loading model...", flush=True)
model = ChatterboxTTS.from_pretrained(device="cuda")

durations = {}
for sid, text in SCENES.items():
    t = time.time()
    wav = model.generate(text, audio_prompt_path=REF, exaggeration=0.5, cfg_weight=0.4)
    path = os.path.join(OUT, f"{sid}.wav")
    ta.save(path, wav, model.sr)
    # exact duration via ffprobe
    dur = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path]).decode().strip())
    durations[sid] = round(dur, 2)
    print(f"{sid}: {dur:.2f}s  ({time.time()-t:.1f}s gen)", flush=True)

with open(os.path.join(OUT, "durations.json"), "w") as f:
    json.dump(durations, f, indent=2)
print("DURATIONS_JSON " + json.dumps(durations), flush=True)
print(f"TOTAL speech: {sum(durations.values()):.1f}s", flush=True)
