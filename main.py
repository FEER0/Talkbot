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
        try: 
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
        except ValueError:
            print('ERROR: This can not be a channel ID. For information oh how to get channelID`s please visit: https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-')
        except AttributeError:
            print('ERROR: The selected channel could not be reached')
        

bot.run(settings.TOKEN)
