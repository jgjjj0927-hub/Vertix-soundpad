import io
import pygame
import sounddevice as sd
import soundfile as sf
from pathlib import Path
from pydub import AudioSegment

SUPPORTED = {".mp3", ".wav", ".ogg", ".flac"}


def load_audio(path: str):
    """читает любой формат в (numpy array, samplerate)"""
    p = Path(path)
    if p.suffix.lower() in (".wav", ".flac"):
        data, sr = sf.read(str(p), dtype="float32")
        return data, sr
    seg = AudioSegment.from_file(str(p))
    buf = io.BytesIO()
    seg.export(buf, format="wav")
    buf.seek(0)
    data, sr = sf.read(buf, dtype="float32")
    return data, sr


class SoundPad:
    def __init__(self, output_device=None):
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            self.ready = True
        except Exception:
            self.ready = False
        self.sounds = []
        self.playing = {}
        self.output_device = output_device

    def list_output_devices(self):
        devices = []
        for i, d in enumerate(sd.query_devices()):
            if d["max_output_channels"] > 0:
                devices.append((i, d["name"]))
        return devices

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
        path = self.sounds[idx]
        try:
            data, sr = load_audio(path)
        except Exception:
            data, sr = None, None
        if data is not None:
            sd.play(data, sr, device=self.output_device)
        else:
            snd = pygame.mixer.Sound(path)
            ch = snd.play()
            if ch is not None:
                self.playing[idx] = ch

    def stop(self, idx: int):
        if idx in self.playing:
            self.playing[idx].stop()
            del self.playing[idx]
        sd.stop()

    def stop_all(self):
        if self.ready:
            pygame.mixer.stop()
        sd.stop()
        self.playing.clear()

осо

soundfile>=0.12
pydub>=0.25

осос

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.audio import SoundPad
from core.license import activate, check_limit
from core.proxy import load_config, save_config, validate_config, start_proxy
from core.effects import apply_echo, mic_test


class VirtuxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("virtux")
        self.geometry("900x600")
        self.configure(bg="#ffffff")
        self.pad = SoundPad()
        self.limit_sounds, self.limit_sec = check_limit()
        self.pinned = False

        self._build_ui()
        self._bind_hotkeys()

    def _build_ui(self):
        top = tk.Frame(self, bg="#ffffff")
        top.pack(fill="x", padx=10, pady=8)
        tk.Button(top, text="+ add sound", command=self.add_sound,
                  bg="#f0f0f0", fg="#000", relief="flat").pack(side="left")
        tk.Button(top, text="pin", command=self.toggle_pin,
                  bg="#f0f0f0", fg="#000", relief="flat").pack(side="left", padx=6)

        self.listbox = tk.Listbox(self, bg="#ffffff", fg="#000",
                                  selectbackground="#7aa2f7", selectforeground="#000",
                                  relief="solid", font=("Consolas", 11))
        self.listbox.pack(fill="both", expand=True, padx=10, pady=6)
        self.listbox.bind("<Double-Button-1>", lambda e: self.play_selected())

        nb = ttk.Notebook(self)
        nb.pack(fill="x", padx=10, pady=6)

        self.settings_tab = tk.Frame(nb, bg="#ffffff")
        self._build_settings(self.settings_tab)
        nb.add(self.settings_tab, text="Settings")

        self.proxy_tab = tk.Frame(nb, bg="#ffffff")
        self._build_proxy(self.proxy_tab)
        nb.add(self.proxy_tab, text="Proxy")

        bottom = tk.Frame(self, bg="#ffffff")
        bottom.pack(fill="x", padx=10, pady=8)
        self.entry_key = tk.Entry(bottom, bg="#ffffff", fg="#000", relief="solid")
        self.entry_key.pack(side="left", fill="x", expand=True)
        tk.Button(bottom, text="activate", command=self.do_activate,
                  bg="#7aa2f7", fg="#000", relief="flat").pack(side="left", padx=6)
        self.status = tk.Label(bottom, text=f"no activation: {self.limit_sounds} sounds / {self.limit_sec}s",
                               bg="#ffffff", fg="#000")
        self.status.pack(side="left", padx=6)

    def _build_settings(self, parent):
        tk.Label(parent, text="echo (ms):", bg="#ffffff", fg="#000").pack(anchor="w", padx=8)
        self.echo_ms = tk.Scale(parent, from_=0, to=1000, orient="horizontal",
                                bg="#ffffff", fg="#000", highlightthickness=0)
        self.echo_ms.pack(fill="x", padx=8)
        tk.Label(parent, text="decay:", bg="#ffffff", fg="#000").pack(anchor="w", padx=8)
        self.echo_decay = tk.Scale(parent, from_=0.0, to=1.0, resolution=0.05,
                                   orient="horizontal", bg="#ffffff", fg="#000",
                                   highlightthickness=0)
        self.echo_decay.pack(fill="x", padx=8)

        tk.Label(parent, text="output device:", bg="#ffffff", fg="#000").pack(anchor="w", padx=8)
        self.device_var = tk.StringVar()
        self.device_combo = ttk.Combobox(parent, textvariable=self.device_var, state="readonly")
        devices = self.pad.list_output_devices()
        self.device_map = {name: idx for idx, name in devices}
        self.device_combo["values"] = [name for _, name in devices]
        self.device_combo.pack(fill="x", padx=8)
        self.device_combo.bind("<<ComboboxSelected>>", self.on_device_change)

        tk.Button(parent, text="test microphone", command=self.test_mic,
                  bg="#f0f0f0", fg="#000", relief="flat").pack(anchor="w", padx=8, pady=6)

    def _build_proxy(self, parent):
        tk.Button(parent, text="load JSON", command=self.load_proxy,
                  bg="#f0f0f0", fg="#000", relief="flat").pack(anchor="w", padx=8, pady=4)
        tk.Button(parent, text="save", command=self.save_proxy,
                  bg="#f0f0f0", fg="#000", relief="flat").pack(anchor="w", padx=8)
        tk.Button(parent, text="start xray", command=self.run_proxy,
                  bg="#f0f0f0", fg="#000", relief="flat").pack(anchor="w", padx=8, pady=4)
        self.proxy_text = tk.Text(parent, height=10, bg="#ffffff", fg="#000", relief="solid")
        self.proxy_text.pack(fill="both", expand=True, padx=8, pady=6)

    def _bind_hotkeys(self):
        self.bind("<Alt_L>", lambda e: self.play_selected())
        self.bind("<Alt_R>", lambda e: self.play_selected())
        self.bind("<Insert>", lambda e: self.toggle_pin())

    def on_device_change(self, event=None):
        name = self.device_var.get()
        self.pad.output_device = self.device_map.get(name)

    def toggle_pin(self):
        self.pinned = not self.pinned
        self.attributes("-topmost", self.pinned)
        self.status.config(text=("pinned" if self.pinned else "unpinned"))

    def add_sound(self):
        if len(self.pad.sounds) >= self.limit_sounds:
            messagebox.showwarning("limit", f"max {self.limit_sounds} sounds without activation")
            return
        path = filedialog.askopenfilename(filetypes=[("audio", "*.mp3 *.wav *.ogg")])
        if path and self.pad.add(path):
            self.listbox.insert("end", Path(path).name)

    def play_selected(self):
        sel = self.listbox.curselection()
        if sel:
            self.pad.play(sel[0])

    def do_activate(self):
        ok, msg = activate(self.entry_key.get().strip())
        messagebox.showinfo("activation", msg)
        if ok:
            self.limit_sounds, self.limit_sec = check_limit()
            self.status.config(text=f"activated: {self.limit_sounds} sounds")

    def test_mic(self):
        level = mic_test(1.5)
        messagebox.showinfo("microphone", f"peak level: {level:.2f}")

    def load_proxy(self):
        path = filedialog.askopenfilename(filetypes=[("json", "*.json")])
        if path:
            self.proxy_text.delete("1.0", "end")
            self.proxy_text.insert("1.0", Path(path).read_text(encoding="utf-8"))

    def save_proxy(self):
        import json
        try:
            cfg = json.loads(self.proxy_text.get("1.0", "end"))
            ok, msg = validate_config(cfg)
            if ok and save_config(cfg):
                messagebox.showinfo("proxy", "saved")
            else:
                messagebox.showerror("proxy", msg)
        except Exception as e:
            messagebox.showerror("proxy", str(e))

    def run_proxy(self):
        ok, msg = start_proxy()
        messagebox.showinfo("xray", msg)


if __name__ == "__main__":
    app = VirtuxApp()
    app.mainloop()



