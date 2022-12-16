import discord
import os


token = os.environ.get("disc_token")
guild_id = os.environ.get("guild_id") or 1052919584287629312

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)

def get_user_from_id(id):
    in_server = client.get_user(int(id))
    guild=client.get_guild(int(guild_id))
    member = guild.get_member(int(id))
    return in_server, member

@client.event
async def on_ready():
    print('Logged in')

async def run():
    await client.start(token)
    


