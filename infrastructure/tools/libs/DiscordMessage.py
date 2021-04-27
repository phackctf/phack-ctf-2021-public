# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Pdrooo
# Created Date: Dec. 2020
# Description : Send single text message from the bot in a team channel
# =============================================================================

from libs.Utils import DISCORD_ID, DISCORD_TOKEN

import libs.CTFd as api

import discord
import os

# Has to be edited manually for the moment
TEAM     = ''
MESSAGE  = ''

client = discord.Client()

# Run discord bot configuration process
def configure():
    client.run( DISCORD_TOKEN )

# Find discord category object by bame
def findCategory(server: discord.Guild, category: str) -> discord.CategoryChannel:
    for c in server.categories:
        if c.name == category:
            return c

    return None

# Find discord text channel object by name
def findChannel(server: discord.Guild, category: discord.CategoryChannel, channel: str) -> discord.TextChannel:
    for c in category.text_channels:
        if c.name == channel:
            return c

    return None

# Send message
@client.event
async def on_ready():

    for server in client.guilds:
        if server.id == DISCORD_ID:

            category  = findCategory(server, 'TEAM')
            chan      = findChannel(server, category, TEAM)

            await chan.send( content = MESSAGE )

            break

    await client.logout()
