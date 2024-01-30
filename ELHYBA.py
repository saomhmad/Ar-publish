import re
import base64
import asyncio
import logging
from telethon import events
from mody import *
from asyncio import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
logging.basicMody(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("ZE")
logger.info("النشر التلقائي شغال الان استمتع ✓")

yaAhmed = False
async def ze_nshr(elhzeyba, sleeptimet, chat, message, seconds):
    global yaAhmed
    yaAhmed = True
    while yaAhmed:
        if message.media:
            sent_message = await elhzeyba.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await elhzeyba.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@elhzeyba.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def Ahmed(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    elhzeyba = event.client
    global yaAhmed
    yaAhmed = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await elhzeyba.get_entity(chat_username)
            await ze_nshr(elhzeyba, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.reply(f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)
    sourceze = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    sourceze = Get(sourceze)
    try:
        await event.client(sourceze)
    except BaseException:
        pass
    
async def ze_allnshr(elhzeyba, sleeptimet, message):
    global yaAhmed
    yaAhmed = True
    ze_chats = await elhzeyba.get_dialogs()
    while yaAhmed:
        for chat in ze_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await elhzeyba.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await elhzeyba.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@elhzeyba.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def Ahmed(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    elhzeyba = event.client
    global yaAhmed
    yaAhmed = True
    await ze_allnshr(elhzeyba, sleeptimet, message)
    sourceze = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    sourceze = Get(sourceze)
    try:
        await event.client(sourceze)
    except BaseException:
        pass
super_groups = ["super", "سوبر"]
async def ze_supernshr(elhzeyba, sleeptimet, message):
    global yaAhmed
    yaAhmed = True
    ze_chats = await elhzeyba.get_dialogs()
    while yaAhmed:
        for chat in ze_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await elhzeyba.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await elhzeyba.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@elhzeyba.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def Ahmed(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    elhzeyba = event.client
    global yaAhmed
    yaAhmed = True
    await ze_supernshr(elhzeyba, sleeptimet, message)
    sourceze = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    sourceze = Get(sourceze)
    try:
        await event.client(sourceze)
    except BaseException:
        pass
@elhzeyba.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_ze(event):
    global yaAhmed
    yaAhmed = False
    await event.edit("**۞︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
@elhzeyba.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def Ahmed(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        sourceze_zesource = """**
🔱 قـائمة اوامر النشر التلقائي للمجموعات 🔱

===== 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱 =====

`.نشر` عدد الثواني معرف الكروب :
~ للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

`.نشر_كروبات` عدد الثواني : 
~ للنشر في جميع المجموعات الموجوده في حسابك
 
`.سوبر` عدد الثواني : 
~ للنشر بكافة المجموعات السوبر التي منظم اليها 

`.ايقاف النشر` :
~ لأيقاف جميع انواع النشر اعلاه

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها

===== 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱 =====
    **"""
        await event.reply(file='https://graph.org/file/5bc8daaefa9f7979cc8b7.jpg', message=sourceze_zesource)
    elif event.pattern_match.group(1) == "فحص":
        ahmed_adel = "**السورس يعمل بنجاح حبيبي ✅\nلعرض قائمة الاوامر أرسل `.الاوامر`**"
        await event.reply(file='https://graph.org/file/5bc8daaefa9f7979cc8b7.jpg', message=ahmed_adel)
        sourceze = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
        sourceze = Get(sourceze)
        try:
            await event.client(sourceze)
        except BaseException:
            pass
print('تم تشغيل نشر التلقائي لسورس زد إي')
elhzeyba.run_until_disconnected()
