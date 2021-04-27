#!/usr/bin/env python3

from PIL import Image
from pyzbar.pyzbar import decode

import os

DIR = './out/'

flagParts = []

# Get flag parts
for i in os.listdir( DIR ):
    image = Image.open( DIR + i )
    data = decode( image )[0].data.decode('utf-8')

    if data[:12] != 'Nothing here':
        flagParts.append(data.split(' '))

# Sort array
flagParts = sorted(flagParts, key = lambda x: int( x[2] ))

# Print flag
for s in flagParts: 
    print(s[4][1:2], end='')

print()