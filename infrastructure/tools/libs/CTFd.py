# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Pdrooo, @Eagleslam
# Created Date: Dec. 2020
# Description : Wrapper over CTFd API to make it more convenient to use
# =============================================================================

from libs.Utils import BColors, CTFD_ACCESS_TOKEN, CTFD_BASE_URL

import requests
import json

headers = {
    'Authorization' : f'Token { CTFD_ACCESS_TOKEN }',
    'Content-Type'  : 'application/json'
}

class Team:
    def __init__(self, obj):
        self.id = obj.get('id')
        self.name = obj.get('name')
        self.members = obj.get('members')
        self.size = len( self.members )

    def ok(self):
        return self.size == 4

    def maybe(self):
        return self.size == 3

    def ko(self):
        return self.size <= 2

class Teams:
    def __init__(self):
        self._stack = []
        self.sizes = [0, 0, 0, 0]

    def add(self, team: Team):
        self._stack.append(team)
        self.sizes[ team.size - 1 ] += 1

    def all(self):
        return self._stack

    def sort(self):
        self._stack.sort( key = lambda x: x.size, reverse = True )

    def ok(self) -> int:
        return self.sizes[3]

    def maybe(self) -> int:
        return self.sizes[2]

    def ko(self) -> int:
        return self.sizes[0] + self.sizes[1]

    def count(self) -> int:
        return len(self._stack)

    def pprint(self) -> str:
        stdout = ''

        for team in self._stack:
            if team.ok():
                stdout += f'{ BColors.OKAY } [+] Equipe \"{ team.name }\" (complet) { BColors.ENDC } { BColors.EOL }'
            elif team.maybe():
                stdout += f'{ BColors.WARN } [~] Equipe \"{ team.name }\" (3/4 members) { BColors.ENDC } { BColors.EOL }'
            elif team.ko:
                stdout += f'{ BColors.FAIL } [-] Equipe \"{ team.name }\" ({ team.size }/4 members) { BColors.ENDC } { BColors.EOL }'

        return stdout

class Stats:
    def __init__(self, sort):
        self.teams = fetchTeams( sort )
        self.players = 0

        for team in self.teams._stack:
            self.players += team.size

    def pprint(self):

        stdout = BColors.EOL
        stdout += '======== TEAMS ========'
        stdout += BColors.EOL
        stdout += self.teams.pprint()
        stdout += BColors.EOL
        stdout += '======== STATS ========'
        stdout += BColors.EOL
        stdout += f'Equipe OK      : { BColors.OKAY } { str( self.teams.ok() ) }/{ str( self.teams.count() ) } { BColors.ENDC } { BColors.EOL }'
        stdout += f'Equipe PRESQUE : { BColors.WARN } { str( self.teams.maybe() ) }/{ str( self.teams.count() ) } { BColors.ENDC } { BColors.EOL }'
        stdout += f'Equipe KO      : { BColors.FAIL } { str( self.teams.ko() ) }/{ str( self.teams.count() ) } { BColors.ENDC } { BColors.EOL }'
        stdout += BColors.EOL
        stdout += f'Total Teams   :  { BColors.BOLD } { str( self.teams.count() ) } { BColors.ENDC } { BColors.EOL }'
        stdout += f'Total Players :  { BColors.BOLD } { self.players } { BColors.ENDC } { BColors.EOL }'
        #stdout += f'Total Users   :  { BColors.BOLD } { self.users } { BColors.ENDC } { BColors.EOL }'
        stdout += f'Space Left    :  { BColors.BOLD } { str( self.teams.count()  * 4 - self.players) } { BColors.ENDC } { BColors.EOL }'
        stdout += '======================'
        stdout +=  BColors.EOL

        return stdout

class Chall:
    def __init__(self, name, category):
        self.name = name
        self.category = category

# Make API Calls
def get(url: str) -> dict:
    raw = requests.get(CTFD_BASE_URL + url, headers =headers)
    return json.loads( raw.text ).get( 'data' )

# Fetch team data
def fetchTeams(sort: bool = False) -> Teams:
    rawTeams = get('/teams')
    teams = Teams()

    # Foreach team
    for team in rawTeams:
        details = get('/teams/' + str(team['id']))

        teams.add( Team( details ) )

    # Sort if necessary
    if sort:
        teams.sort()

    return teams

# Fetch CTF global stats
def fetchStats(sort: bool = False) -> Stats:
    stats = Stats(sort)

    return stats
