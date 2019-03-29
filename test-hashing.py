#!/usr/bin/env python3
from stbx_hash import encode, decode, hash

# buf = bytes.fromhex('deadbeeffeedcafebabec0de')
buf = bytes.fromhex('446563656e7472616c697a652065766572797468696e672121')
s = encode(buf)

import multibase as mb
print(mb.encode('base16', buf).decode('ascii'))
print(mb.encode('base32', buf).decode('ascii'))
print(decode(s))
print(decode(s).hex())
print(mb.encode('base32', s).decode('ascii'))
print(s)

def b16compage(a, b):
    a_base16ascii = mb.encode('base16', a).decode('ascii')
    b_base16ascii = mb.encode('base16', b).decode('ascii')
    return b_base16ascii == a_base16ascii

def decode_over_encode(buf):
    a = buf
    b = decode(encode(a))
    return b16compage(a,b)

assert(decode_over_encode(buf))
assert(decode_over_encode(bytes()))
assert(decode_over_encode(bytes([])))
assert(decode_over_encode(bytes([1])))
assert(decode_over_encode(bytes([255])))
assert(decode_over_encode(bytes([255,255])))
assert(decode_over_encode(bytes([255,255,128])))
assert(decode_over_encode(bytes([255,255,0,128])))
assert(decode_over_encode(bytes([255,255,0])))
assert(decode_over_encode(bytes([255,255,0,0])))
assert(decode_over_encode(bytes([127])))
assert(decode_over_encode(bytes([127,0])))

# It does not seem to support leading zeros!
# All of the following fail the test:
#
# assert(decode_over_encode(bytes([0,0,127,128,255,255,0])))
# assert(decode_over_encode(bytes([0,0])))
# assert(decode_over_encode(bytes([0])))
# assert(decode_over_encode(bytes([0,127,0])))
# assert(decode_over_encode(bytes([0,127])))

print(hash(encode(buf)))