import json
import random
import requests
import logging

logger = logging.getLogger(__name__)


def get_members_voice(context):
    if context.message.author.voice:
        voice_channel = context.message.author.voice.channel
        all_members = voice_channel.members
        if not all_members:
            return None
        else:
            no_bots = list(filter(lambda x: not x.bot, all_members))
            list_of_names = list(map(lambda x: x.name, no_bots))
            return list_of_names
    else:
        return None


