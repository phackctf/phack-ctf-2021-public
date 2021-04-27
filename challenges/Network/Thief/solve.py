#! /usr/bin/python3

import os, base64, json

os.system("tshark -nr dns.pcapng -T fields -e dns.qry.name -Y 'dns.qry.name contains \".phack.fr\"' | uniq > /tmp/domains.txt")
domains = open("/tmp/domains.txt").readlines()
os.system("rm /tmp/domains.txt")

flag = [''] * len(domains)

for domain in domains:

    decoded = bytes.fromhex(domain.strip().replace(".phack.fr", "")).decode('utf-8')
    data = json.loads(decoded)
    index = data['index']
    char = data['data']
    flag[int(index) - 1] = char

print(''.join(map(str, flag)))
