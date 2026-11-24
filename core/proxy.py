import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent / "base"
BASE.mkdir(exist_ok=True)
PROXY_FILE = BASE / "proxy.json"
XRAY_DIR = BASE / "xray"

DEFAULT_CONFIG = {
    "dns": {"queryStrategy": "UseIPv4", "servers": ["https://8.8.8.8/dns-query"]},
    "inbounds": [
        {"listen": "127.0.0.1", "port": 10808, "protocol": "socks",
         "settings": {"auth": "noauth", "udp": True}, "tag": "socks"}
    ],
    "outbounds": [{"protocol": "freedom", "tag": "direct"}],
    "routing": {"domainStrategy": "AsIs", "rules": []},
}

def save_config(cfg: dict) -> bool:
    try:
        PROXY_FILE.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
        return True
    except Exception:
        return False

def load_config() -> dict:
    if PROXY_FILE.exists():
        try:
            return json.loads(PROXY_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return DEFAULT_CONFIG.copy()

def validate_config(cfg: dict) -> tuple[bool, str]:
    if "inbounds" not in cfg or "outbounds" not in cfg:
        return False, "нет inbounds/outbounds"
    for ib in cfg["inbounds"]:
        if "port" not in ib or "protocol" not in ib:
            return False, "inbound без port/protocol"
    return True, "ок"

def start_proxy() -> tuple[bool, str]:
    exe = XRAY_DIR / ("xray.exe" if sys.platform == "win32" else "xray")
    if not exe.exists():
        return False, "xray не найден в base/xray/"
    try:
        subprocess.Popen([str(exe), "-c", str(PROXY_FILE)],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True, "запущен"
    except Exception as e:
        return False, str(e)
