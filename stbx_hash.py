#!/usr/bin/env python3

import hashlib
import multihash
import multibase

# https://github.com/multiformats/multicodec/blob/master/table.csv
BLAKE2s224 = 0xb25c

# encode : buf -> multibase
def encode(buf):
    return multibase.encode('base58btc', buf).decode('ascii')

# decode : multibase -> buf
def decode(multibaseString):
    return multibase.decode(multibaseString)

# hash : multibase -> multibase
def hash(multibaseString):
    b = decode(multibaseString)
    mh = hashB(b)
    mb = encode(mh)
    return mb

# hashB : buffer -> buffer
def hashB(buf):
    # setup blake2s hash function on input buffer
    m = hashlib.blake2s(buf, digest_size=28)
    # print("digest size = %d bits" % (m.digest_size * 8))
    # print("block size = %d ??" % m.block_size)
    
    # compute digest buffer
    d = m.digest()

    # wrap in multihash tag
    mh = multihash.encode(d, BLAKE2s224)
    return mh

# buf = bytes([0,0,0,255])
# mbuf =  encode(buf)
# m = hash(mbuf)
# print(m)