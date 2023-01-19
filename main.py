import disnake
import re

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

yes_words = ['ДА', 'Да', 'дА', 'да', 'смешно', 'смешной']
when_words = ['Когда', 'когда']
user = ['User', 'user']

@bot.event
async def on_ready():
    print('Бот работает, кекв')

def simplify_word(word):
    last_letter = ''
    result = ''
    for letter in word:
        if letter != last_letter:
            last_letter = letter
            result += letter
            result = re.sub(r'[.,"\'-?:!;]', '', result)
    return result

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg_words = [simplify_word(word) for word in message.content.split()]

    # для каждого слова првоеряем, содержится ли оно в запрещенном списке
    for word in msg_words:
        if word in yes_words:
            await message.channel.send('Нет')
            return
        elif word in when_words:
            await message.channel.send('Послезаврта')
            return
        elif word in user:
            await message.channel.send(f'<@{user_id}> -- Вот он')
            return


bot.run('bot_id')