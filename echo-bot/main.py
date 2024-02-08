from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
import asyncio
from config import BOT_TOKEN,DB_PATH
BOT_USERNAME: Final = "@remomirbot"

#commands

async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Hello, Thanks for texting me, I'm banannaaaa")

async def help_command(update: Update, context:Contexttypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a banana who can help yoyyy!!!")

async def custom_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!!")



# handles Responses
    
def handle_responses(text:str) -> str:
    processed: str = text.lower()
    if "hello" in text:
        return "Hey there"
    if "I'm Remo" in text:
        return "Welcome boss!"
    if "I'm Akshay" in text:
        return "Fuck off bastard"
    
async def handle_message(update: Update, ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == "group":
        if BOT_USERNAME
