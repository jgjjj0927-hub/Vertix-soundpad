import sqlite3
import hashlib
import hmac
import os
import secrets
import string
from pathlib import Path
from datetime import datetime, timedelta

BASE = Path(__file__).parent.parent / "base"
BASE.mkdir(exist_ok=True)
DB = BASE / "licenses.db"
SECRET_FILE = BASE / ".secret"

PREFIX_POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY_DAYS = {"trial": 7, "month": 30, "for_good": 0}  # 0 = бессрочно

def get_secret() -> bytes:
    if not SECRET_FILE.exists():
        SECRET_FILE.write_bytes(os.urandom(32))
    return SECRET_FILE.read_bytes()

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS licenses (
            key TEXT PRIMARY KEY,
            type TEXT NOT NULL,
            days INTEGER DEFAULT 0,
            created_at TEXT NOT NULL,
            activated_at TEXT,
            machine_id TEXT,
            active INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def machine_id() -> str:
    import platform, uuid
    raw = f"{platform.node()}-{uuid.getnode()}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]

def _raw_key() -> str:
    """генерирует FRA-192"""
    prefix = "".join(secrets.choice(PREFIX_POOL) for _ in range(3))
    number = f"{secrets.randbelow(1000):03d}"
    return f"{prefix}-{number}"

def _sign(raw: str) -> str:
    sig = hmac.new(get_secret(), raw.encode(), hashlib.sha256).hexdigest()[:6].upper()
    return f"{raw}-{sig}"

def create_key(key_type: str, days: int = None) -> str:
    """создаёт уникальный одноразовый ключ вида FRA-192-AB12CD"""
    init_db()
    if days is None:
        days = KEY_DAYS.get(key_type, 0)
    conn = sqlite3.connect(DB)
    while True:
        raw = _raw_key()
        key = _sign(raw)
        exists = conn.execute("SELECT 1 FROM licenses WHERE key=?", (key,)).fetchone()
        if not exists:
            break
    conn.execute(
        "INSERT INTO licenses (key, type, days, created_at) VALUES (?, ?, ?, ?)",
        (key, key_type, days, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()
    return key

def verify_key(key: str) -> bool:
    """проверяет HMAC-подпись, не трогая базу"""
    parts = key.split("-")
    if len(parts) != 3:
        return False
    raw = f"{parts[0]}-{parts[1]}"
    expected = hmac.new(get_secret(), raw.encode(), hashlib.sha256).hexdigest()[:6].upper()
    return hmac.compare_digest(parts[2], expected)

def activate(key: str) -> tuple[bool, str]:
    if not verify_key(key):
        return False, "неверный формат ключа"
    init_db()
    mid = machine_id()
    conn = sqlite3.connect(DB)
    row = conn.execute(
        "SELECT type, days, activated_at, machine_id, active FROM licenses WHERE key=?",
        (key,),
    ).fetchone()
    if not row:
        conn.close()
        return False, "ключ не найден"
    ltype, days, activated_at, saved_mid, active = row
    if active:
        conn.close()
        if saved_mid == mid:
            return False, "ключ уже активирован на этой машине"
        return False, "ключ одноразовый, уже использован"
    conn.execute(
        "UPDATE licenses SET activated_at=?, machine_id=?, active=1 WHERE key=?",
        (datetime.now().isoformat(), mid, key),
    )
    conn.commit()
    conn.close()
    return True, f"активирован: {ltype}"

def check_limit() -> tuple[int, int]:
    """(лимит звуков, лимит секунд). без активации — 15/15"""
    init_db()
    conn = sqlite3.connect(DB)
    row = conn.execute(
        "SELECT type, days, activated_at FROM licenses WHERE active=1 AND machine_id=?",
        (machine_id(),),
    ).fetchone()
    conn.close()
    if not row:
        return 15, 15
    ltype, days, activated_at = row
    if ltype in ("month", "trial") and activated_at:
        expiry = datetime.fromisoformat(activated_at) + timedelta(days=days)
        if datetime.now() > expiry:
            return 15, 15
    limits = {"trial": (50, 60), "month": (9999, 99999), "for_good": (99999, 999999)}
    return limits.get(ltype, (15, 15))
