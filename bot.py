import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["8496775244:AAEyM5uJEijzDiZmLRJv6ctr03i7X9dYQM8"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hola, tu pedido está siendo consultado. Pronto verás el estatus."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 Bot en ejecución...")
app.run_polling()
