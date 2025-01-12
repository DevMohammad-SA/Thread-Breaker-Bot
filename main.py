import os
import textwrap

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


def break_message(message, max_length=230):
    return textwrap.wrap(message, width=max_length)


async def start(update: Update, context: ContextTypes):
    await update.message.reply_text("Hello! I am a bot to break long messages into smaller ones. Send me a message and I will break it into smaller messages for you.")


async def handle_message(update: Update, context: ContextTypes):
    message = update.message.text
    if message:
        print(f"Received message: {message}")
        await update.message.reply_text("Breaking message into smaller parts...")
    x = 1
    for part in break_message(message):
        await update.message.chat.send_chat_action("typing")
        await update.message.reply_text(f"`[{x}]\n{part}`", parse_mode="MarkdownV2")
        x += 1


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(poll_interval=1)


if __name__ == "__main__":
    main()
