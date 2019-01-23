import statebox_pb2 as stbx

import binascii

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