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
    AFROTOO = "M_9_T"
    await bot.send_message(AFROTOO, "** نور الحاكم تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع ميوزك نور الحاكم وارسال رسالة للمطور⚡🚦.")
    await idle()
from pyrogram import Client, errors

# تعريف عميل Pyrogram
app = Client("my_bot")

# دالة لمعالجة الرسائل الواردة
@app.on_message()
async def handle_message(client, message):
    try:
        # محاولة استرجاع معرّف النظير
        peer = await client.resolve_peer(-1002206384889)
        # استخدام معرّف النظير لعمليات إضافية
        await client.send_message(peer, "Hello from Pyrogram!")
    except errors.PeerIdInvalid:
        print("Invalid peer ID provided.")
    except errors.PeerIdNotFound:
        print("Peer ID not found in database.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# تشغيل التطبيق
app.run()
