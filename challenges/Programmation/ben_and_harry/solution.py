#!/usr/bin/env python3

import socket
import json

HOST = 'ben-and-harry.phack.fr'
PORT = 1664

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while 1:

        data = s.recv(512).decode('utf-8').rstrip()

        try:
            json_data = json.loads(data.split('\n')[0])
        except:
            print(data)
            break

        base = json_data['b']
        encoded_data = json_data['code']

        base10 = ""

        for n in encoded_data.split(' '):
            base10 += chr(int(str(n), base))

        s.sendall(base10.encode('utf-8'))
