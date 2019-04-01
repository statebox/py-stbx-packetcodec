# for the tx codec
import statebox_pb2 as stbx
import binascii

# for hashing & buffer<=>string conversion
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

def makeFiringTransaction(previousHash, executionHash, messageHex, transition):
    # construct transaction from these parameters
    tx = stbx.Transaction(
        previous = binascii.a2b_hex(previousHash),
        firing = stbx.Firing(
            execution = binascii.a2b_hex(executionHash),
            message = binascii.a2b_hex(messageHex),
            path = [transition]
        )
    )
    encoded = tx.SerializeToString() # protocol buffer output (bytes)
    return binascii.b2a_hex(encoded) # convert to hex string

