# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Pdrooo
# Created Date: Dec. 2020
# Description : Send vpn configs to teams private channels
# =============================================================================

from libs.Utils import DISCORD_ID, DISCORD_TOKEN, VPN_CONFIG_DIR

import libs.CTFd as api

import discord
import os

MESSAGE = '''\
_

🚩  **Salut l'équipe !**  🚩

Voilà vos configurations VPN pour pouvoir accéder à votre environnement de challenges.

**Let's flag now !**  🤙

_
'''

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

# Send config using bot
@client.event
async def on_ready():

    for server in client.guilds:
        if server.id == DISCORD_ID:
            category = findCategory(server, 'TEAM')
            
            _, dirs, _ = next(os.walk( VPN_CONFIG_DIR ))

            # Foreach team
            for d in dirs:
                
                # Do not send config for admin vm
                if d == 'admin':
                    continue

                _, _, filenames = next(os.walk(f'{ VPN_CONFIG_DIR }/{ d }'))
                chan = findChannel(server, category, d)
                attach = []

                # Foreach file in team folder
                for fn in filenames:
                    attach.append(
                        discord.File(
                            fp = f'{ VPN_CONFIG_DIR }/{ d }/{ fn }',
                            filename = fn
                        )
                    )
                # Send first mesage
                await chan.send( 
                    content = MESSAGE,
                    files = attach
                )

            break

    await client.logout()