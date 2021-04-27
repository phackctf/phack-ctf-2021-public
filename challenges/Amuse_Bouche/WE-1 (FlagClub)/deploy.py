#!/usr/bin/env python3

import discord

# DISCORD_ID = 0000      # Production server (removed)
DISCORD_ID = 0000        # POC Server (removed)

DISCORD_TOKEN = ''

WELCOME = '''\
_

🚩 **[ Bonjour CTFeurs et CTFeuses ! ]** 🚩

Je vous transmets ce message que je viens de recevoir à votre attention :

```
La première règle du Flag Club est : il est interdit de parler du Flag Club.
La seconde règle du Flag Club est : il est interdit de parler du Flag Club.
Troisième règle du Flag Club : rassemblez cinq morceaux de secret pour reconstituer le flag.
Quatrième règle : les points rapportés par ce challenge uniquement seront dégressifs, en fonction du nombre de résolution.
Cinquième règle : coopérer ou non, mentir ou dire la vérité, la décision vous revient.
Sixième règle : pour ce challenge uniquement, les échanges d'informations entre les équipes sont autorisés.
Septième règle : le challenge continuera aussi longtemps que nécessaire.

    - Adi Shamir
```

Était également joint ceci :

```
{}
```

**Voyez ce que vous pouvez en tirer !** 🤙

_
'''

client = discord.Client()

# Find discord category object by bame
def findCategory(server: discord.Guild, category: str) -> discord.CategoryChannel:
    for c in server.categories:
        if c.name == category:
            return c

    return None

# Send the chall
@client.event
async def on_ready():
    lines = []

    with open('flag.parts') as f:
        while r := f.readline():
            lines.append(r.rstrip())

    for server in client.guilds:
        if server.id == DISCORD_ID:
            category = findCategory(server, 'TEAM')

            for i, chan in enumerate(category.text_channels):
                await chan.send( WELCOME.format( lines[i] ) )

    await client.logout()

client.run( DISCORD_TOKEN )
