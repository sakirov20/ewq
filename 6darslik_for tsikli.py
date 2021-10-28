import time

from telethon import TelegramClient, connection
from telethon.sync import TelegramClient, events
#   we need to change the connection ^^^^^^^^^^
api_id = 7108918
api_hash = "dece7611717647a28d7ac863c8224658"

with TelegramClient('998905414956', api_id, api_hash, proxy=('mtproxy.dinazflowers.com', 443, '100c9b906b76db839efec81b12cb8c80')) as client:
   client.send_message('me', 'Hello, myself!')
   #print(client.download_profile_photo('@lite_pro'))

   @client.on(events.NewMessage(pattern=r'(?i).*Ретв'))
   async def handler(event):
      await event.click(1, -1)
      time.sleep(10)
    #  await event.reply('Задания')


   @client.on(events.NewMessage(pattern=r'(?i).*Подпи'))
   async def handler(event):
       await event.click(1, -1)
       time.sleep(10)
  #    await event.reply('Задания')

   @client.on(events.NewMessage(pattern=r'(?i).*Доступны новые задания!', func=lambda e: e.is_private))
   async def handler(event):
       message = await event.reply('Задания')
       await asyncio.wait([message.delete()])


   @client.on(events.NewMessage(pattern=r'(?i).*Постав'))
   async def handler(event):
       await event.click(1, -1)
       time.sleep(10)
      # await event.reply('Задания')




   client.run_until_disconnected()
