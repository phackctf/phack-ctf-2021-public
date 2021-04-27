#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import *
import base64

capture = rdpcap('dump.pcapng')
ping_data = ""

for packet in capture:
   if packet[ICMP].type == 8: # Echo request
       ping_data += packet.load.decode('utf-8')

print(ping_data)
