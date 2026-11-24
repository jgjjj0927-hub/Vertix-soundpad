import pygame
from pathlib import Path

SUPPORTED = {".mp3", ".wav", ".ogg"}

class SoundPad:
    def __init__(self):
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            self.ready = True
        except Exception:
            self.ready = False
        self.sounds = []
        self.playing = {}

    def add(self, path: str) -> bool:
        if not self.ready:
            return False
        p = Path(path)
        if p.suffix.lower() not in SUPPORTED:
            return False
        self.sounds.append(str(p))
        return True

    def play(self, idx: int):
        if not self.ready or not (0 <= idx < len(self.sounds)):
            return
        snd = pygame.mixer.Sound(self.sounds[idx])
        ch = snd.play()
        if ch is not None:
            self.playing[idx] = ch

    def stop(self, idx: int):
        if idx in self.playing:
            self.playing[idx].stop()
            del self.playing[idx]

    def stop_all(self):
        if self.ready:
            pygame.mixer.stop()
        self.playing.clear()
