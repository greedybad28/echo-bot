from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
from config import BOT_TOKEN,DB_PATH
BOT_USERNAME: Final = "@remomirbot"



#commands 

async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Hello, Thanks for texting me, I'm banannaaaa")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a banana who can help yoyyy!!!")

async def custom_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!!")
# bomb script below 
for i in range(1000):
    bomb = i * "*\n"


# handles Responses
    
def handle_responses(text: str) -> str:
    processed: str = text
    if "hello" in processed:
        return "Hey there"
    elif "I'm Remo" in processed:
        return "Welcome boss!"
    elif "I'm Akshay" in processed:
        return "Fuck off bastard"
    elif "I'm Vyuha" in processed:
        return bomb
    elif "Mombti" in processed:
        return "https://t.me/intpchatmbti"
    else:
        return "Tf are you talking about"
    
async def handle_message(update: Update,context: ContextTypes.DEFAULT_TYPE):
        message_type: str = update.message.chat.type
        text: str = update.message.text

        print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

        if message_type == "group":
            if BOT_USERNAME in text:
                return
                # new_text: str = text.replace(BOT_USERNAME,"").strip()
                # response: str = handle_responses(new_text)
            else:  
                return
        else:
            response: str = handle_responses(text)
        print("Bot:", response)
        await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    print("App has started")

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    #messages

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #errors
    app.add_error_handler(error)

    app.run_polling(poll_interval=3)
    





