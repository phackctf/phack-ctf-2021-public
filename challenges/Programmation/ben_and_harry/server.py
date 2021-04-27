#!usr/bin/python3

import threading
import socket
import sys
import signal
import random
import json
import string

FLAG = "PHACK{Av3z-v0us-L3s-b4s3s?}"
HOST = ''
PORT = 1664

STEPS_COUNT = 12
threads = []

SENTENCES = [
"V0us 3t3s en v4c4nc3s?",
"JOy3uses P'Hack!",
"VOus n'4v3z p4s l3s B4ses.",
"M4is a quOi ca s3rt l4 b4s3 12?",
"Ca f4it b34uc0up de 1 Et d3 0",
"Et dir3 que c3rt4ins f0n7 du b4se jump1ng",
"Sin0n c4 v4 v0us?",
"Tu 4im3s pytH0n? Te4m 2.7 oU T3am 3.9?",
"Le CTF de p'H4ck! F477ait l4 tr0uv3r c3ll3 l4!",
"Au f4it, p0rt3z-bi3n v05 m4squ3s!",
"L3s cl0ch3s s0n7 p4ssEes",
"Un Kind3r_M4xi 3st c4ché s0uS l'aRbr3",
"Un ch0c0l4t c0ntr3 l3 fl4g, d3Al?"
]


def keyboardInterruptHandler(signal, frame):
    sys.exit(0)


def get_random_base():
    return random.randint(2, 16)


def get_random_sentence():
    return SENTENCES[random.randrange(0, len(SENTENCES))]


def encode(base, sentence):
    return ' '.join(frm(ord(x), base) for x in sentence)


def frm(x, b):
    assert(x >= 0)
    assert(1< b < 37)
    r = ''

    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r


def worker(conn):

    counter = 0
    running = True

    while running:
        base = get_random_base()
        sentence = get_random_sentence()

        encoded_sentence = encode(base, sentence)
        message = "Answer me!" if counter == 0 else "Yes! One more."
        response = {"b" : base, "code" : encoded_sentence, "msg" : message}

        conn.sendall((json.dumps(response) + "\n>>> ").encode('utf-8'))
        data = conn.recv(1024).decode("utf-8").rstrip()

        if sentence == data:
            counter += 1
        else:
            conn.sendall(("✞ Nope, wrong answer..." + "\n").encode('utf-8'))
            running = False

        if counter == STEPS_COUNT:
            conn.sendall(("Yeah! Well done. Here is the flag : " + FLAG + "\n").encode('utf-8'))
            running = False

    conn.close()


def main():

    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST, PORT))
        s.listen(10)
        conn, addr = s.accept()

        print('[*] Client connected with ' + addr[0] + ':' + str(addr[1]) + ' on port ' + str(PORT))

        t = threading.Thread(target=worker, args=(conn,))
        threads.append(t)
        t.start()


if __name__ == "__main__":

    signal.signal(signal.SIGINT, keyboardInterruptHandler)

    main()
