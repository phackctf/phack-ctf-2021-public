#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Eagleslam
# Created Date: Jan. 2021
# Description : Solve challenge A-Maze-Ing
# =============================================================================

import requests
import json
import os
import sys

LENGTH = 21

r = requests.get("http://a-maze-ing.phack.fr:4242/chall")
json = json.loads(r.content)
token = json['token']
maze = json['solveMe']


def display_maze(matrix):
    global LENGTH
    to_display = ""

    for j in range(0, len(matrix[0])  ):
        for i in range(0, len(matrix)  ):
            to_display += matrix[i][j]

        to_display += '\n'

    print(to_display)


def send_response(solution, token):
    print("Sending : " + str(solution))
    mydata = {"token": str(token), "solution": str(solution) }
    #print(mydata)
    r = requests.post("http://a-maze-ing.phack.fr:4242/chall", json = mydata)
    print(r.content)


def solve(matrix):

    solution = ""
    user = (1,1)

    display_maze(matrix)
    next_move = find_next_move(matrix, user)

    while next_move != "WON" and next_move != "FAILED":
        if next_move == "RIGHT":
            user = (user[0] + 1, user[1])
            solution += "→"
        elif next_move == "LEFT":
            user = (user[0] - 1, user[1])
            solution += "←"
        elif next_move == "UP":
            user = (user[0], user[1]-1)
            solution += "↑"
        elif next_move == "DOWN":
            user = (user[0], user[1]+1)
            solution += "↓"

        if matrix[user[0]][user[1]] != "$":
            matrix[user[0]][user[1]] = "."

        os.system("clear")
        display_maze(matrix)
        next_move = find_next_move(matrix, user)

    if next_move == "FAILED":
        print("We have failed, man")
        sys.exit(1)

    return solution


def find_next_move(matrix, user):

    if matrix[user[0]][user[1]] == "$":
        return "WON"
    elif matrix[user[0]][user[1] + 1] == " " or matrix[user[0]][user[1] + 1] == "$":
        return "DOWN"
    elif matrix[user[0] + 1][user[1]] == " " or matrix[user[0] + 1][user[1]] == "$":
        return "RIGHT"
    elif matrix[user[0] - 1][user[1]] == " " or matrix[user[0] - 1][user[1]] == "$":
        return "LEFT"
    elif matrix[user[0]][user[1] - 1] == " " or matrix[user[0]][user[1] - 1] == "$":
        return "UP"
    else:
        return "FAILED"


def create_maze_matrix(maze):
    global LENGTH

    matrix = []
    for i in range(LENGTH):
        matrix.append(['.' for j in range(len(maze) / LENGTH)])

    x = 0
    y = 0

    for i in range(0, len(maze)):
        if i >= LENGTH and i % LENGTH == 0:
            y += 1
            x = 0

        matrix[x][y] = str(maze[i])
        x += 1

    return matrix


matrix = create_maze_matrix(maze)
solution = solve(matrix)
send_response(solution, token)
