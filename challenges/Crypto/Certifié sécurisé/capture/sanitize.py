#!/usr/bin/env python3

# Remove "sensible" data from capture file

find = [
    b'\x70\xfc\x8f\x9e\x18\xc4',    # Freebox name
    b'\x46\x74\x2c'                 # Intel mac address
]

replace = [
    b'\x70\xfc\x8f\x00\xca\xfe',
    b'\x42\x42\x42'
]

with open('capture.pcapng', 'rb') as f:
    file = f.read()
    file = file.replace(find[0], replace[0])
    file = file.replace(find[1], replace[1])

    with open('out.pcap', 'wb') as out:
        out.write(file)
