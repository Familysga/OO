from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="29400566",
    api_hash="8fd30dc496aea7c14cf675f59b74ec6f",
    bot_token="6711048210:AAGeTTCLCXyBmcgcgC264YPkmI5g5xBJSnQ",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    AFROTOO = "H_8_o"
    await bot.send_message(AFROTOO, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
