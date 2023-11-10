from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantRequest
import re
from dotenv import load_dotenv
import os
 
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE')
username=os.getenv('USERNAME')
group_link=os.getenv('GROUP_LINK')
user_id=os.getenv('USER_ID')
client = TelegramClient(username, api_id, api_hash)
dico=[]
async def main():


    await client.start(phone=phone_number)

    channel_to_scan = await client.get_entity(int(group_link))
    group_to_send = await client.get_entity('https://t.me/MaestroSniperBot')

       
    async def scan(event):
        contract = re.search(r'0x\w+', event.message.text)
        if contract:
            print(contract.group(0))
            print("sending message")
            await client.send_message(group_to_send,contract.group(0))

    @client.on(events.NewMessage(chats=channel_to_scan))
    async def handle_new_message(event):
        print(event)
        sender = await event.get_sender()
        if int(user_id)==sender.id:
            await scan(event)
        else:
            print("pas lui")        

    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())