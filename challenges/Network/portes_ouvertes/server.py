#!usr/bin/python3

import threading
import socket
import sys
import signal

FLAG = "PHACK{s4cr3_c0ur4nt_d'R}"
HOST = ''
PORTS = [5916, 5689, 5690, 5036, 5116, 5969, 5345, 5851, 5039, 5000, 5022, 5012, 5555, 5888, 5750, 5684, 5795, 5698, 5478, 5321, 5864, 5127, 5695, 5568, 5986, 5987] 

LOGO = '''
                                 ,╦╦NNNN╦╦╥,
                             ╔Nª╨"        `"╙╩N╦
                          ╔Ñ╨`                  ╙╬╦
                        ╦Ñ^                       `╚N,
                      ╔╫^                            -ª,
                    ╔╫╨                                ^Φ
                   éÅ                                     N
                 ,╬M                                      `╬╕
                ╓╫╛                                         ╬╦
               ╓╫^      ,   ╬╫Ω   ╔,   ╔K╕   ╓Φ╫╬ ╔╫╫╓╬╫Å    ╙¼
              ╓╫`     ╬╫Ñ╬Ñ⌐╙^Ñ╫  ╫╫ ╔╫Ñ╫╫.╔╫╬╨   ╬╫╫╫Ö       ²H
             ,╬      ╬╫╫╫╫Å`  ╫╫D╬╫╫.╫Ñ╬Ñ╫Ñ╙╫╦╦╦╦:╫╫`"╩ÑÑ╛     ²Ñ
             ╬Ñ      ╟╫H     ╘╫Ñ  ╩╛╙Å   ╙`  ```` `             ╙N
            ╟╬        `                ,,,,.,,╔╦w        ╗╬╬╕    `¼
           ,╫⌐   d╬N,           ╓╦╫╬╬╫╫╫Ñ╨╚╫╫M"²        ╬╫╫╫╫     "U
           ╬H    ╫╫╫╫N        ╓╫Ñ╨    ╔╫⌐ ß╬╫╬ÑM       ╬╫╫╫╫╫H     `
          ╔╫     ╫╫╫╫╫╫╕      ²╫╦╦╦╦  ╬Ñ   ╫          ╔╫╫╫╫╫╫N
          ╬Ñ     ╫╫╫╫╫╫╫╕       ````   ²              ╫╫╫╫╫╫╫╡      ╘¡
          ╫H     ╟╫╫╫╫╫╫╫                     ,╔╦╦w  .╫╫╫╫╫╫╫⌐       ╙
         j╫       ╫╫╫╫╫╫╫╬   ╔╬╫╫╫Kw       ,╦╬╫╫╫╫╫╬ ╔╫╫╫╫╫╫Å         ╕
         ╔╫       ²╫╫╫╫╫╫╫N ╔╫╫╫╫╫╫╫╫╬K╦╦D╫╫╫╫╫╫╫╫╫╫╫╬╫╫╫╫╫╬
         ╚Ñ        ²╫╫╫╫╫╫╫╦╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫Å           H
         ╚╫          ╟╫╫╫╫╫╫╫╫╫╫ÑÑÑ╩╩╨╨╙╙"""""╙╙╙╨╩╩╬╫╫╫╫╨            H
         '╫⌐          `╬╫╫╫╫╫╬╦NDDÑÑÑ╬╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫ÑÑÑÑM═       j
          ╬N       %ÑÑÑ╩╩╩╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫Ñ             Å
          '╫              ╫╫╫╫╫╫╫Ö"╫╫╫╫╫╫╫╫╫╫╫╫,╟╫╫╫╫╫╫╫            ╔
           ╟Ñ             ╬╫╫╫╫╫╫╫╫╫╫╫╫╫╫Ñ╬╫╫╫╫╫╫╫╫╫╫╫╫Ñ           ,╛
            ╟╬            ╙╫╫╫╫╫╫╫╫╫╫╫╫╫Nj╫╫╫╫╫╫╫╫╫╫╫╫╫           ╔╛
             ╚╫╕           ╙╫╫╫╫╫╫╫╫╫╫╫╫╫╬╫╫╫╫╫╫╫╫╫╫╫╩           ╔`
              ╙╫╕            "╩Ñ╫╫╫╫╫╫╫Ñ╩"╩ÑÑÑÑ╩╩╨^²           ,╝
                ╙Nw                                           é^
                  ╙╫╦                                      ╓m^
                    ╙╬N╥                                ,╦Å`
                       "╩╬N╥.                       ,╗Ñ╩"
                           `╙╬╬N╦,            ²╔╦ΦÑ╨"
                                ``"╙╙╨╨╩╩╩╩╨╙^`


                                   .Bonjour.
'''
threads = []

def get_flag_part(i):
    if i < int(len(FLAG)/2):
        return ('.' * i * 2) + (FLAG[i*2:(i*2)+2]) + ('.' * 2 * int((len(FLAG)/2) - i))
    else:
        return 'There is nothing here... ¯\_(ツ)_/¯'


def keyboardInterruptHandler(signal, frame):
    sys.exit(0)


def worker(num):
    global HOST
    port = PORTS[num]

    print("[*] Server listening on port %s %d" %(HOST, (port)))

    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST, port))
        s.listen(10)
        conn, addr = s.accept()

        print('[*] Client connected with ' + addr[0] + ':' + str(addr[1]) + ' on port ' + str(port))
        conn.sendall((get_flag_part(num) + "\n").encode('utf-8'))
        conn.close()


def response_to_http_port():
    global HOST, LOGO
    port = 80

    print("[*] Server listening on port %s %d" %(HOST, (port)))

    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((HOST, port))
        s.listen(10)
        conn, addr = s.accept()

        print('[*] Client connected with ' + addr[0] + ':' + str(addr[1]) + ' on port ' + str(port))
        conn.sendall((LOGO + "\n").encode('utf-8'))
        conn.close()


def main():

    for i in range(len(PORTS)):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    t = threading.Thread(target=response_to_http_port)
    threads.append(t)
    t.start()

if __name__ == "__main__":

    assert len(FLAG) % 2 == 0

    signal.signal(signal.SIGINT, keyboardInterruptHandler)

    main()
