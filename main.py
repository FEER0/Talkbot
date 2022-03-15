import settings
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="..", intents = intents, help_command= None)

@bot.listen()
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    global channelID
    while 1 == 1:
        channelID = int(input('Enter channel id: '))
        channel = bot.get_channel(channelID)
        print(f'Channel id {channelID} has been selected')
        run = True
        while run == True:
            message = input('Enter message or exit: ')
            if message == 'exit':
                run = False
                break
            await channel.send(message)

@bot.listen()
async def on_message(message):
    if message.author == bot.user or message.channel.id != channelID:
        print(message.author.display_name + ": " + message.content)

bot.run(settings.TOKEN)