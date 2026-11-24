import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from core.license import create_key

TOKEN = "8642013882:AAEzxfy1TrMzNOhRcKz0hv7QHmvpg33UHyw"
ADMIN_ID = 8224529558

KEY_DAYS = {"trial": 7, "month": 30, "for_good": 0}

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("no access")
        return
    kb = [
        [InlineKeyboardButton("trial", callback_data="trial"),
         InlineKeyboardButton("month", callback_data="month")],
        [InlineKeyboardButton("for_good", callback_data="for_good"),
         InlineKeyboardButton("custom", callback_data="custom")],
    ]
    await update.message.reply_text("choose key type:", reply_markup=InlineKeyboardMarkup(kb))

async def on_button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "custom":
        await q.edit_message_text("send: /custom 365")
        return
    days = KEY_DAYS.get(q.data, 0)
    key = create_key(q.data, days)
    await q.edit_message_text(f"key ({q.data}):\n`{key}`", parse_mode="Markdown")

async def custom(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    try:
        days = int(ctx.args[0])
    except (IndexError, ValueError):
        await update.message.reply_text("format: /custom 365")
        return
    key = create_key("custom", days)
    await update.message.reply_text(f"key (custom {days}d):\n`{key}`", parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("custom", custom))
    app.add_handler(CallbackQueryHandler(on_button))
    app.run_polling()

if __name__ == "__main__":
    main()
