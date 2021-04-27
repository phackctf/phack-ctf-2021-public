#!/usr/bin/env python3

from uuid import uuid4

import qrcode
import random
import os

FLAG = "PHACK{MaaaYb3_Th1s_Waas_Overk1lL?!}"
FAKE = 1928

def qrCodeFactory(data):
    code = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_Q,
        box_size = 10,
        border = 4,
    )

    code.add_data(data)
    code.add_data(junk())
    code.make(fit = True)

    return code.make_image(fill_color = "black", back_color = "white")

def junk():
    return ' (id = 0x%s)' % uuid4().hex

stack = []

for i in range( len(FLAG) ):
    text = f'Flag char { i } is "{ FLAG[i] }"'
    stack.append( qrCodeFactory(text) )

for i in range( FAKE ):
    text = f'Nothing here'
    stack.append( qrCodeFactory(text) )

random.shuffle(stack)

os.system("rm -rf ./out > /dev/null")
os.system("mkdir ./out > /dev/null")
for i in range( len(stack) ):
    stack[i].save( f'out/code{i}.png' )
os.system("zip out/data.zip out/*.png ")
os.system("rm -rf ./out/*.png > /dev/null")
