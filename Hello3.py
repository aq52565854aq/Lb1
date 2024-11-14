from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

api_id = 29373321
api_hash = '82006f9f2326d0417b0d63dc09eb05f0f'
phone = '+380950084362'
client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start()

    channel_username = ('my_bot78')
    channel = await client.get_entity(channel_username)

    participants = await client(GetParticipantsRequest(
        channel,
        ChannelParticipantsSearch(''),
        offset=0,
        limit=2,
        hash=0
    ))

    for user in participants.users:
        print(user.id, user.first_name, user.last_name)

    await client.send_message(channel, message='Hello, world!')

with client:
    client.loop.run_until_complete(main())