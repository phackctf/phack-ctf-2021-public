#!/usr/bin/env python3

import socket

HOST = 'journees-portes-ouvertes.phack.fr'

flag_parts = []
PORTS = [5916, 5689, 5690, 5036, 5116, 5969, 5345, 5851, 5039, 5000, 5022, 5012, 5555, 5888, 5750, 5684, 5795, 5698, 5478, 5321, 5864, 5127, 5695, 5568, 5986, 5987]

for port in PORTS:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        data = s.recv(512)
        flag_parts.append(data.decode('utf-8').rstrip())


flag = ""

for index in range(50):
    for part in flag_parts:
        if "¯\_(ツ)_/¯" not in part and len(part) > index and part[index] != ".":
            flag += part[index]

print("Flag : " + flag)
