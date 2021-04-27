#!/usr/bin/env python3
import random
import os

# Test challenge by doing random combinations

lines = []
with open('flag.parts', 'r') as f:
    while line := f.readline():
        lines.append(line.rstrip())

random.shuffle(lines)

while len(lines) >= 5:
    tmp = []
    for i in range(5):
        tmp.append(lines.pop())
        
    chunks = '\n'.join(tmp)
    os.system(f'echo "{chunks}" | ssss-combine -t 5')
