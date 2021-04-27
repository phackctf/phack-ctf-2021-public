#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Pdrooo
# Created Date: Dec. 2020
# Description : A maze solving puzzle.
# =============================================================================

from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask, Response, request
from uuid import uuid4
from libs.Maze import Maze
from threading import Lock

import datetime
import json
import time
import re
import os

# Global config
FLAG          = 'PHACK{M4zEs_4Re_7rUly_4m@zIng}'
GRID_SIZE     = 10
TIME_TO_SOLVE = 5

HELP_MESSAGE = f'''
<pre>
<h1>routes</h1>

| Route  | Method |
|--------|--------|
| /      | GET    |
| /chall | GET    |
| /chall | POST   |
| /flag  | GET    |

<h1>rules</h1>

Hello x,

Your goal today is to rob the bank.
But the police is fast, you have { TIME_TO_SOLVE } sec to reach the vault and grab the cash.

Good luck !
'''

# Maze instance pool
pool  = []

# Background pool managment
sched = BackgroundScheduler()
app   = Flask(__name__)

# Pool access lock
mutex = Lock()

# ---------------------------- #
#            WEBAPP            #
# ---------------------------- #

# -- Root Index
@app.route('/', methods=['GET'])
def help():

    return Response(
        response = HELP_MESSAGE,
        status = 200
    )

# -- Gentle troll
@app.route('/flag', methods=['GET'])
def loliflag():

    return Response(
        response = 'Lol, seriously ?',
        status = 200
    )

# -- Get maze
@app.route('/chall', methods=['GET'])
def getChall():
    maze, token = registerMaze()

    return Response(
        response = json.dumps({ "token" : token, "solveMe" : maze.buildAsciiMaze() }),
        status = 200,
        mimetype = 'application/json'
    )

# -- Submit solution
@app.route('/chall', methods=['POST'])
def solveChall():
    try:
        token = request.json.get('token')
        data  = request.json.get('solution')

    except:
        return Response(
            response = 'Expected json format : { "token" : "", "solution" : "" }',
            status = 401,
        )

    return Response(
        response = solve(token, data),
        status = 200,
        mimetype = 'application/json'
    )

# -------------------------- #
#            MAZE            #
# -------------------------- #

# -- Remove maze from valid pool
def deleteMaze(entry):
    with mutex:
        pool.remove(entry)

# -- Generate maze and add in valid pool
def registerMaze():
    token = uuid4().hex
    maze  = Maze( GRID_SIZE )

    trigger = datetime.datetime.now() + datetime.timedelta( seconds = TIME_TO_SOLVE )

    with mutex:
        pool.append((token, maze))

        sched.add_job(deleteMaze, 'date', run_date=trigger, args=[(token, maze)])

    return maze, token

# -- Check solution validity
def solve(token, data):

    # Token exists ?
    with mutex:
        match = [i for i in pool if i[0] == token]

    if not len(match):
        return 'Wrong token or time is over'
    elif len(match) > 1:
        return 'Too many token usage.\n Please contact administrator.'

    # Data in proper format ?
    if re.match('^[↑↓←→]*$', data) == None:
        return '"Solution" field must match "^[↑↓←→]*$"'

    # Solution is valid ?
    if match.pop()[1].solve(data):
        return f'Congrats ! The flag is { FLAG }'
    else:
        return 'Not a valid solution. Try again !'

# -- Entrypoint
if __name__ == '__main__':
    sched.start()
    app.run('0.0.0.0', os.environ['CHALL_PORT'], False)
