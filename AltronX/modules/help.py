from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, SUDO_USERS, CMD_HNDLR as hl
from telethon import events, Button


PythonHelp = f"â ðð®ð½ð¤ð© ððð¡ð¥ ððð£ðª â\n\nÂ» **á´ÊÉªá´á´ á´É´ Êá´Êá´á´¡ Êá´á´á´á´É´ê± ê°á´Ê Êá´Êá´**\nÂ» **á´á´á´ á´Êá´á´á´Ê: @ItzExStar**"


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  "https://te.legra.ph/file/07d39b85c6cea32f15259.jpg",
                                  caption=PythonHelp,
                                  buttons=[
           [
            Button.inline("â¢ ê±á´á´á´ â¢", data="spam"),
            Button.inline("â¢ Êá´Éªá´ â¢", data="raid"),
           ],
           [
            Button.inline("â¢ á´xá´Êá´ â¢", data="extra"),
           ],
           [    
            Button.url("â¢ á´á´á´á´á´á´ê± â¢", "https://t.me/TheAltron"),
            Button.url("â¢ sá´á´á´á´Êá´ â¢", "https://t.me/AltronChats")
           ],
           ],
           )


extra_msg = f"""
**Â» á´xá´Êá´ á´á´á´á´á´É´á´ê±:**

ð¨ðð²ð¿ðð¼ð: á´ê±á´ÊÊá´á´ á´á´á´ê±
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd

ðð°ðµð¼: á´á´ á´á´á´Éªá´ á´ á´á´Êá´ á´É´ á´É´Ê á´ê±á´Ê
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

ðð²ð®ðð²: á´á´ Êá´á´á´ á´ É¢Êá´á´á´/á´Êá´É´É´á´Ê
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group


**Â© @ItzExStar**
"""

                 
raid_msg = f"""
**Â» Êá´Éªá´ á´á´á´á´á´É´á´ê±:**

ð¥ð®ð¶ð±: á´á´á´Éªá´ á´á´á´ê± Êá´Éªá´ á´É´ á´É´Ê ÉªÉ´á´Éªá´ Éªá´á´á´Ê á´ê±á´Ê ê°á´Ê É¢Éªá´ á´É´ Êá´É´É¢á´.
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

ð¥ð²ð½ð¹ðð¥ð®ð¶ð±: á´á´á´Éªá´ á´á´á´ê± Êá´á´ÊÊ Êá´Éªá´ á´É´ á´Êá´ á´ê±á´Ê!!
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

ðð¥ð²ð½ð¹ðð¥ð®ð¶ð±: á´á´á´á´á´Éªá´ á´á´á´ê± Êá´á´ÊÊ Êá´Éªá´ á´É´ á´Êá´ á´ê±á´Ê!!
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

ðððð¢ð: Êá´á´ á´ Êá´Éªá´ á´É´ á´Êá´ á´ê±á´Ê!!
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

ðððð¢ð: ê±Êá´Êá´ÊÉª Êá´Éªá´ á´É´ á´Êá´ á´ê±á´Ê!!
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

ðððð¢ð: á´Êá´á´ Êá´Éªá´ á´É´ á´Êá´ á´ê±á´Ê!!
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>


**Â© @ItzExStar**
"""

spam_msg = f"""
**Â» ê±á´á´á´ á´á´á´á´á´É´á´ê±:**

ð¦ð½ð®ðº: ê±á´á´á´ê± á´ á´á´ê±ê±á´É¢á´.
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>

ð£ð¼ð¿ð»ð¦ð½ð®ðº: á´á´Êá´á´É¢Êá´á´ÊÊ ê±á´á´á´.
  1) {hl}pspam <count>

ðð®ð»ð´: ê±á´á´á´ê± Êá´É´É¢ÉªÉ´É¢ á´á´ê±ê±á´É¢á´ ê°á´Ê É¢Éªá´ á´É´ á´á´á´É´á´á´Ê.
  1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)


** Â© @ItzExStar**
"""                     
           
           
@MK1.on(events.CallbackQuery(pattern=r"help_back"))
@MK2.on(events.CallbackQuery(pattern=r"help_back"))
@MK3.on(events.CallbackQuery(pattern=r"help_back"))
@MK4.on(events.CallbackQuery(pattern=r"help_back"))
@MK5.on(events.CallbackQuery(pattern=r"help_back"))
@MK6.on(events.CallbackQuery(pattern=r"help_back"))
@MK7.on(events.CallbackQuery(pattern=r"help_back"))
@MK8.on(events.CallbackQuery(pattern=r"help_back"))
@MK9.on(events.CallbackQuery(pattern=r"help_back"))
@MK10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            PythonHelp,
            buttons=[
           [
            Button.inline("â¢ ê±á´á´á´ â¢", data="spam"),
            Button.inline("â¢ Êá´Éªá´ â¢", data="raid"),
           ],
           [
            Button.inline("â¢ á´xá´Êá´ â¢", data="extra"),
           ],
           [
            Button.url("â¢ á´á´á´á´á´á´ê± â¢", "https://t.me/TheAltron"),
            Button.url("â¢ sá´á´á´á´Êá´ â¢", "https://t.me/AltronChats")
           ],
           ],
        )           
   else:
        await event.answer("Make Your Own Altron Bots !! @TheAltron", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"spam"))
@MK2.on(events.CallbackQuery(pattern=r"spam"))
@MK3.on(events.CallbackQuery(pattern=r"spam"))
@MK4.on(events.CallbackQuery(pattern=r"spam"))
@MK5.on(events.CallbackQuery(pattern=r"spam"))
@MK6.on(events.CallbackQuery(pattern=r"spam"))
@MK7.on(events.CallbackQuery(pattern=r"spam"))
@MK8.on(events.CallbackQuery(pattern=r"spam"))
@MK9.on(events.CallbackQuery(pattern=r"spam"))
@MK10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(spam_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            ) 
   else:
        await event.answer("Make Your Own Altron Bots !! @TheAltron", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"raid"))
@MK2.on(events.CallbackQuery(pattern=r"raid"))
@MK3.on(events.CallbackQuery(pattern=r"raid"))
@MK4.on(events.CallbackQuery(pattern=r"raid"))
@MK5.on(events.CallbackQuery(pattern=r"raid"))
@MK6.on(events.CallbackQuery(pattern=r"raid"))
@MK7.on(events.CallbackQuery(pattern=r"raid"))
@MK8.on(events.CallbackQuery(pattern=r"raid"))
@MK9.on(events.CallbackQuery(pattern=r"raid"))
@MK10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )  
     else:
        await event.answer("Make Your Own Altron Bots !! @TheAltron", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"extra"))
@MK2.on(events.CallbackQuery(pattern=r"extra"))
@MK3.on(events.CallbackQuery(pattern=r"extra"))
@MK4.on(events.CallbackQuery(pattern=r"extra"))
@MK5.on(events.CallbackQuery(pattern=r"extra"))
@MK6.on(events.CallbackQuery(pattern=r"extra"))
@MK7.on(events.CallbackQuery(pattern=r"extra"))
@MK8.on(events.CallbackQuery(pattern=r"extra"))
@MK9.on(events.CallbackQuery(pattern=r"extra"))
@MK10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
   else:
        await event.answer("Make Your Own Altron Bots !! @TheAltron", cache_time=0, alert=True)
