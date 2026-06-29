#!/usr/bin/env python3
"""Re-roll a single scene until its duration is within an expected range."""
import os, subprocess, sys
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

REF = "/home/sanjayg4/chatterbox/refs/storytelling.wav"
OUT = "/home/sanjayg4/dba-knowledge-base/video-src/audio"
SID = "s6"
TEXT = "Start anywhere. Follow a course, trace a concept, or simply ask, and get answers in plain language."
LO, HI = 7.0, 12.0   # acceptable seconds
MAX_TRIES = 6

model = ChatterboxTTS.from_pretrained(device="cuda")
best = None
for i in range(1, MAX_TRIES + 1):
    wav = model.generate(TEXT, audio_prompt_path=REF, exaggeration=0.45, cfg_weight=0.5)
    dur = wav.shape[-1] / model.sr
    print(f"try {i}: {dur:.2f}s", flush=True)
    if best is None or dur < best[0]:
        best = (dur, wav)
    if LO <= dur <= HI:
        best = (dur, wav)
        break
ta.save(os.path.join(OUT, f"{SID}.wav"), best[1], model.sr)
final = float(subprocess.check_output(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration",
     "-of", "csv=p=0", os.path.join(OUT, f"{SID}.wav")]).decode().strip())
print(f"SAVED {SID}: {final:.2f}s", flush=True)
