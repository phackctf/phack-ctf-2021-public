from scapy.all import *
import time

flag = "PHACK{p1n9_p0n9_p1n9_p0n9_qu1_4_d3j4_j0u3_4u_73nn15_d3_74813_?}"

for c in flag:
    send( IP(dst="192.168.13.37") / ICMP(type="echo-request", id=0x123) / Raw(load=c),verbose=0)
    time.sleep(1)
