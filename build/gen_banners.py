from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).parent.parent
ICON_ICO = ROOT / "assets" / "icon.ico"
ICON_SVG = ROOT / "assets" / "icon.svg"
OUT = ROOT / "build"

BG = (26, 26, 26)       # #1a1a1a
ACCENT = (122, 162, 247)  # #7aa2f7

def load_icon():
    if ICON_ICO.exists():
        return Image.open(ICON_ICO).convert("RGBA")
    # fallback: если ico нет, берём svg через cairosvg
    try:
        import cairosvg
        import io
        png = cairosvg.svg2png(url=str(ICON_SVG), output_width=256, output_height=256)
        return Image.open(io.BytesIO(png)).convert("RGBA")
    except Exception:
        # последний fallback — просто квадрат
        img = Image.new("RGBA", (256, 256), ACCENT + (255,))
        return img

def try_font(size):
    for name in ("segoeui.ttf", "arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def make_banner():
    img = Image.new("RGB", (493, 58), BG)
    draw = ImageDraw.Draw(img)
    icon = load_icon().resize((48, 48), Image.LANCZOS)
    img.paste(icon, (16, 5), icon)
    font = try_font(22)
    draw.text((80, 16), "virtux", fill=ACCENT, font=font)
    img.save(OUT / "installer_banner.bmp", "BMP")
    print("installer_banner.bmp")

def make_dialog():
    img = Image.new("RGB", (493, 312), BG)
    draw = ImageDraw.Draw(img)
    icon = load_icon().resize((128, 128), Image.LANCZOS)
    x = (493 - 128) // 2
    y = (312 - 128) // 2 - 20
    img.paste(icon, (x, y), icon)
    font = try_font(28)
    text = "virtux"
    tw = draw.textlength(text, font=font)
    draw.text(((493 - tw) / 2, y + 150), text, fill=ACCENT, font=font)
    img.save(OUT / "installer_dialog.bmp", "BMP")
    print("installer_dialog.bmp")

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    make_banner()
    make_dialog()
    print("готово")
