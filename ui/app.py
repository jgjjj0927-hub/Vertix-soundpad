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
        self.configure(bg="#1a1a1a")
        self.pad = SoundPad()
        self.limit_sounds, self.limit_sec = check_limit()
        self.pinned = False

        self._build_ui()
        self._bind_hotkeys()

    def _build_ui(self):
        top = tk.Frame(self, bg="#1a1a1a")
        top.pack(fill="x", padx=10, pady=8)
        tk.Button(top, text="+ добавить звук", command=self.add_sound,
                  bg="#2a2a2a", fg="#fff", relief="flat").pack(side="left")
        tk.Button(top, text="📌 закрепить", command=self.toggle_pin,
                  bg="#2a2a2a", fg="#fff", relief="flat").pack(side="left", padx=6)

        self.listbox = tk.Listbox(self, bg="#111", fg="#ccc", selectbackground="#7aa2f7",
                                  relief="flat", font=("Consolas", 11))
        self.listbox.pack(fill="both", expand=True, padx=10, pady=6)
        self.listbox.bind("<Double-Button-1>", lambda e: self.play_selected())

        nb = ttk.Notebook(self)
        nb.pack(fill="x", padx=10, pady=6)

        self.settings_tab = tk.Frame(nb, bg="#1a1a1a")
        self._build_settings(self.settings_tab)
        nb.add(self.settings_tab, text="Settings")

        self.proxy_tab = tk.Frame(nb, bg="#1a1a1a")
        self._build_proxy(self.proxy_tab)
        nb.add(self.proxy_tab, text="Proxy")

        bottom = tk.Frame(self, bg="#1a1a1a")
        bottom.pack(fill="x", padx=10, pady=8)
        self.entry_key = tk.Entry(bottom, bg="#111", fg="#fff", relief="flat")
        self.entry_key.pack(side="left", fill="x", expand=True)
        tk.Button(bottom, text="активировать", command=self.do_activate,
                  bg="#7aa2f7", fg="#000", relief="flat").pack(side="left", padx=6)
        self.status = tk.Label(bottom, text=f"без активации: {self.limit_sounds} звуков / {self.limit_sec}с",
                               bg="#1a1a1a", fg="#888")
        self.status.pack(side="left", padx=6)

    def _build_settings(self, parent):
        tk.Label(parent, text="эхо (мс):", bg="#1a1a1a", fg="#ccc").pack(anchor="w", padx=8)
        self.echo_ms = tk.Scale(parent, from_=0, to=1000, orient="horizontal",
                                bg="#1a1a1a", fg="#ccc", highlightthickness=0)
        self.echo_ms.pack(fill="x", padx=8)
        tk.Label(parent, text="затухание:", bg="#1a1a1a", fg="#ccc").pack(anchor="w", padx=8)
        self.echo_decay = tk.Scale(parent, from_=0.0, to=1.0, resolution=0.05,
                                   orient="horizontal", bg="#1a1a1a", fg="#ccc",
                                   highlightthickness=0)
        self.echo_decay.pack(fill="x", padx=8)
        tk.Button(parent, text="проверить микрофон", command=self.test_mic,
                  bg="#2a2a2a", fg="#fff", relief="flat").pack(anchor="w", padx=8, pady=6)

    def _build_proxy(self, parent):
        tk.Button(parent, text="загрузить JSON", command=self.load_proxy,
                  bg="#2a2a2a", fg="#fff", relief="flat").pack(anchor="w", padx=8, pady=4)
        tk.Button(parent, text="сохранить", command=self.save_proxy,
                  bg="#2a2a2a", fg="#fff", relief="flat").pack(anchor="w", padx=8)
        tk.Button(parent, text="запустить xray", command=self.run_proxy,
                  bg="#2a2a2a", fg="#fff", relief="flat").pack(anchor="w", padx=8, pady=4)
        self.proxy_text = tk.Text(parent, height=10, bg="#111", fg="#ccc", relief="flat")
        self.proxy_text.pack(fill="both", expand=True, padx=8, pady=6)

    def _bind_hotkeys(self):
        self.bind("<Insert>", lambda e: self.toggle_pin())

    def toggle_pin(self):
        self.pinned = not self.pinned
        self.attributes("-topmost", self.pinned)
        self.status.config(text=("закреплено" if self.pinned else "откреплено"))

    def add_sound(self):
        if len(self.pad.sounds) >= self.limit_sounds:
            messagebox.showwarning("лимит", f"максимум {self.limit_sounds} звуков без активации")
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
        messagebox.showinfo("активация", msg)
        if ok:
            self.limit_sounds, self.limit_sec = check_limit()
            self.status.config(text=f"активировано: {self.limit_sounds} звуков")

    def test_mic(self):
        level = mic_test(1.5)
        messagebox.showinfo("микрофон", f"пиковый уровень: {level:.2f}")

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
                messagebox.showinfo("прокси", "сохранено")
            else:
                messagebox.showerror("прокси", msg)
        except Exception as e:
            messagebox.showerror("прокси", str(e))

    def run_proxy(self):
        ok, msg = start_proxy()
        messagebox.showinfo("xray", msg)

if __name__ == "__main__":
    app = VirtuxApp()
    app.mainloop()
