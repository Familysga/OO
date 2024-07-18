from pyrogram import Client

# قراءة المتغيرات من ملف .env
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

app = Client(
    "my_bot_session",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=os.getenv("BOT_TOKEN")
)

@app.on_message()
async def echo(client, message):
    await message.reply_text(message.text)

if name == "main":
    app.run()