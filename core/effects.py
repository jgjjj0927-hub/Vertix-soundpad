import numpy as np
import sounddevice as sd

def apply_echo(data: np.ndarray, delay_ms: int, decay: float) -> np.ndarray:
    data = data.astype(np.float32)
    delay = int(44100 * delay_ms / 1000)
    if delay >= len(data):
        return data
    out = data.copy()
    for i in range(delay, len(data)):
        out[i] += out[i - delay] * decay
    return out

def mic_test(duration: float = 2.0) -> float:
    rec = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype="float32")
    sd.wait()
    return float(np.abs(rec).max())
