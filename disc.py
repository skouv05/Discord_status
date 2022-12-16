import discord
import os
import serial
token = os.environ.get("disc_token")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)

def get_user_from_id(id):
    in_server = client.get_user(int(id))
    guild=client.get_guild(1052919584287629312)
    member = guild.get_member(int(id))
    return in_server, member

@client.event
async def on_ready():
    print('Logged in')


client.run(token)

serial.write('\x03')
