from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="15837209",
    api_hash="fe081df6989a4d79c1004903bb4f23e6",
    bot_token="6525182940:AAHVo-EPIHrKMYXa5CyfI53_BcHVkhw80bI",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    AFROTOO = "K_o_c_1"
    await bot.send_message(AFROTOO, "** نور الحاكم تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع ميوزك نور الحاكم وارسال رسالة للمطور⚡🚦.")
    await idle()
