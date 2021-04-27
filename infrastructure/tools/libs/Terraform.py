# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Pdrooo
# Created Date: Dec. 2020
# Description : Teams VM terraform ressource generation
# =============================================================================

from jinja2 import Template
from libs.Utils import VPN_CONFIG_DIR

import libs.CTFd as api

import difflib
import os

# Remove 
def sanitize(username: str) -> str:
    username = username.lower()
    username = ''.join(filter(lambda x: (x.isalpha() or x.isdigit()), username))

    return username

# Returns most likely folder match to ctfd team name
def match(team: str, dirs: list) -> str:
    # Uppercases and dots seems to be offending
    # for the matching algo so let's remove them.
    team = team.lower()
    team = team.replace('.', '-')

    # Even when multiple match, the first one seems to be the
    # closest one.
    return difflib.get_close_matches(team, dirs)[0]

# Generate terraform
def generate() -> str:

    # Sanitized teams / users
    teams = []

    # Get teams from CTFd
    stack = []
    rawTeams = api.fetchTeams()
    for team in rawTeams.all():
        players = []
        for memb in team.members:
            name = api.get('/users/' + str(memb)).get('name')
            players.append( name )
    
        stack.append((team.name, players))
    
    # Get teams vpn out dirs
    _, dirs, _ = next(os.walk( VPN_CONFIG_DIR ))

    # Clean team names / usernames to make it tag / discord complient
    # and match destination folder.

    for row in stack:
        teams.append((
            match(row[0], dirs),
            [ sanitize(x) for x in row[1] ]
        ))

    # Generate terraform ressources from jinja template.

    template = Template(open('templates/teams.tf.j2').read())
    return template.render(teams = teams)