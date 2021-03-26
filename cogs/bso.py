import asyncio
import discord
import os
import random
import logging

from discord.ext import commands


VOTE_REACT = {"yes": "✅", "no": "❌", "time": "🔟", "half_time": "5️⃣", "stop": "🛑"}
VOTE_TIME = 10

logger = logging.getLogger(__name__)
BSO = {"ingos": {"series": "РРР", "range": iter(range(5050110021, 5050110041))},}

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def get(self, ctx, *, insure=None):
        if insure:
            i = iter(BSO[insure.casefold()]["range"])
            some = next(i)
            if some:
                await ctx.send(f'{BSO[insure.casefold()]["series"]} {some}')
        else:
            await ctx.send(list(BSO.keys()))





def setup(bot):
    bot.add_cog(Commands(bot))
