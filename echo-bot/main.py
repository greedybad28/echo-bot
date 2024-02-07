from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
import asyncio
import config
from config import BOT_TOKEN,DB_PATH,ADMINS



print(config.BOT_TOKEN)

