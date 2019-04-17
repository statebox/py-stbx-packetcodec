# for the tx codec
import statebox.statebox_pb2 as stbx
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

def hashHex(hexString):
    b = binascii.a2b_hex(hexString)
    mb = hashB(b)
    return encode(mb)

def makeFiringTransaction(previousHash, executionHash, messageHex, transition):
    executionBuf = None;
    if (executionHash and (executionHash != b"")):
        executionBuf = decode(executionHash)
    # construct transaction from these parameters
    tx = stbx.Transaction(
        previous = decode(previousHash),
        firing = stbx.Firing(
            execution = (executionBuf and executionBuf or None),
            message = (messageHex and binascii.a2b_hex(messageHex) or None),
            path = [transition]
        )
    )
    encoded = tx.SerializeToString() # protocol buffer output (bytes)
    return binascii.b2a_hex(encoded).decode('ascii') # convert to hex string

# decoding is not needed, as for now the APi takes care of this
# def decodeTx(txHex):
#     encoded = binascii.a2b_hex(txHex)
#     decoded = stbx.Transaction.FromString(encoded)
#     print(decoded)