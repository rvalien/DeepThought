import discord
import logging
import random

from discord.ext import commands

logger = logging.getLogger(__name__)


class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener("on_message")
    async def word_react(self, message):
        trigger_words = {
            "извините": "ПИРОЖКИ!!!",
            "сколько в": "ДА СКОЛЬКО В ТЕБЕ ЖИЗНИ?",
            }

        if not message.author.bot:
            word = next((value for key, value in trigger_words.items() if key in message.content.casefold()), None)
            if word:
                await message.channel.send(word)
                await self.bot.process_commands(message)

    @commands.Cog.listener("on_message")
    async def add_reaction(self, message):
        react_dict = {
            "алло": "📞",
            "окно": "🪟",
            " 123": "🛎️",
            "спать": random.choice(["💤", "😪", "🥱", "🛌", "🛏️"]),
        }

        if not message.author.bot:
            emoji = next((value for key, value in react_dict.items() if key in message.content.casefold()), None)
            if emoji:
                await message.add_reaction(emoji)
                await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(Listener(bot))
