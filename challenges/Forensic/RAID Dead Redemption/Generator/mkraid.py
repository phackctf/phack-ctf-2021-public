#!/usr/bin/env python3.8

from os import listdir

"""
    >> P'Hack CTF <<

    Author: Pedrooo
    Date: 09/12/2020
    Description: Simple fake RAID 5 generator using 1 byte chunk size.

"""

class Raid():
    def __init__(self, ndisk: int):
        self.ndisk = ndisk
        self.ndata = ndisk - 1

        self.buffer = bytearray()

    # Store new file in RAID
    def store(self, file: str):
        with open(file, 'rb') as f:
            self.buffer += bytearray( f.read() )

    # Export to outfile
    def export(self):
        parity = self.ndata
        dataset = [ bytearray() for i in range(self.ndisk) ]
        
        # Create disks buffers in memory
        while (chunk := self.popHead(self.ndata)):

            index = [ x for x in range( self.ndisk ) if x != parity]

            dataset[parity] += self.xorAll(chunk)
            
            for i, ch in zip(index, chunk):
                dataset[i] += bytes([ ch ])

            # Next parity disk
            parity = (parity - 1) % 3

        # Write buffers in files
        for i in range( self.ndisk ):
            with open(f'./bin/DISK{i+1}.bin', 'wb') as f:
                f.write( dataset[i] )

    # Pop `nbytes' first bytes of buffer
    def popHead(self, nbytes: int) -> bytearray:
        head = self.buffer[:nbytes]
        self.buffer = self.buffer[nbytes:]

        return self.pad(head) if len(head) > 0 else False

    # Add padding
    def pad(self, b: bytearray) -> bytearray:
        return b + (b'\x00' * (self.ndata - len(b)))

    # Xor all bytes in `b'
    @classmethod
    def xorAll(cls, b: bytearray) -> bytes:
        if len(b) > 2:
            return cls.xor( b[0], cls.xorAll( b[1:] ) )
        elif len(b) < 2:
            raise ValueError('Cannot xor less thab 2 val')

        return cls.xor( b[0], b[1] )

    # Xor 2 bytes
    @staticmethod
    def xor(b1: bytes, b2: bytes) -> bytes:
        return bytes([ b1 ^ b2 ])

# Entrypoint

if __name__ == "__main__":   
    raid = Raid( 3 )
    
    for f in listdir('./images'):
        raid.store( f'./images/{f}' )
    
    raid.export()