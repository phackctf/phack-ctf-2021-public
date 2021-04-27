# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Pdrooo
# Created Date: Dec. 2020
# Description : Create teams roles, text channels, voice channels, and send
#   welcome message
# =============================================================================

from libs.Utils import DISCORD_ID, DISCORD_TOKEN, VPN_CONFIG_DIR

import libs.CTFd as api

import discord

WELCOME = '''\
_

🚩  **Bienvenue dans votre channel d'équipe !**  🚩

Vous êtes les seuls à pouvoir lire les messages qui seront envoyés ici, à l'exception des **admins** qui sont bien entendu omnipotents par essence.
Il est possible que nous passions de temps en temps prendre des nouvelles, mais si vous avez **un besoin d'aide** pressant vous pouvez nous mentionner
sans problème par un petit @Admin.

**Bon CTF  !**  🤙

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
            print('foud')
            return c
    print('not found')
    return None

# Sanitize team name to make it discord ready
def sanitize(name: str) -> str:
    spaceme = ['.', '_', '/', '\\', '\'']
    removeme = ['<', '>', '(', ')']

    for x in spaceme:
        name = name.replace(x, ' ')

    for x in removeme:
        name = name.replace(x, '')

    return name.rstrip().lstrip()

# Is team already created ?
def exists(server: discord.Guild, user: str) -> bool:
    roles = server.roles

    for role in roles:
        if role.name == user:
            return True

    return False

async def run():
    await client.wait_until_ready()

# Let's create !
@client.event
async def on_ready():
    
    for server in client.guilds:
        if server.id == DISCORD_ID:

            teams    = api.fetchTeams()                 # Fetch teams from CTFd
            category = findCategory(server, 'TEAM')     # Retrieve text channel category
            blabla   = findCategory(server, 'BLABLA')   # Retrieve voice channel cetegory

            # Foreach team
            for team in teams.all():
                name = sanitize(team.name)

                # Skip if team already exists
                if exists(server, name):
                    print('team ' + name + ' already exist')
                    continue
                else:
                    print('Team [' + name + '] does not exist. Will create.')

                # Create team role
                role = await server.create_role( name = name )
                
                overwrites = {
                    server.default_role : discord.PermissionOverwrite( view_channel = False ),
                    server.me : discord.PermissionOverwrite( view_channel = True ),
                    role : discord.PermissionOverwrite( view_channel = True )
                }

                # Create team text-channel
                chan = await server.create_text_channel( name = name, overwrites = overwrites, category = category )
                
                # Create team voice-channel
                await server.create_voice_channel( name = name, overwrites = overwrites, category = blabla )

                # Send welcome mesage
                await chan.send( 'https://tenor.com/view/jason-mantzoukas-the-house-greetings-welcome-gif-8225006' )
                await chan.send( WELCOME )

            break

    await client.logout()