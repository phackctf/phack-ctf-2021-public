import hashlib

#   +---+  +---+  +---+
#   | 0 |  | 1 |  | 2 |  
#   +---+  +---+  +---+
#   +---+  +---+  +---+
#   | 3 |  | 4 |  | 5 |  
#   +---+  +---+  +---+
#   +---+  +---+  +---+
#   | 6 |  | 7 |  | 8 |  
#   +---+  +---+  +---+

seq = b'\x00\x04\x01\x03\x07\x06\x05\x08'

def sha1(data):
    return hashlib.sha1(data).digest()

with open('android/data/system/gesture.key', 'wb') as f:
    f.write(sha1(seq))