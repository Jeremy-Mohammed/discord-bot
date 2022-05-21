import discord
from discord.ext import commands
import music

cogs = [music]

clients = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTc2NzA2MTIwNzE2NTUwMTQ0.GgNw4u.8VAVpof7cVbO44c1CSvm-ZlABPNXxAp1tK6xPM")

print("hi")