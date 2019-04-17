# Statebox Python library

## Usage

This module handles conversion between buffers and strings and computing a hash digest.

- Buffer <=> String encoding is Base58 BTC
- Hash function used is: BLAKE2s, 224 bits
- This is stored as multihash

It also provides encoding of firing transactions.

```python
import statebox

txHex = statebox.makeFiringTransaction("deadbeef", "feedc0de", "cafebabe", 0)
print(txHex) # => b'0a04deadbeef120e0a04feedc0de10001a04cafebabe'
```

## API

**Note**: must use Python 3.6+!

### Make transaction

- `makeFiringTransaction(previousHash, executionHash, messageHex, transition)`

### String to buffer and back

- encode : buf -> multibase
- decode : multibase -> buf

Turn buffer into multibase encoded ascii string

```python
>>> from stbx_hash import encode
>>> print(encode(bytes.fromhex('7fff39')))
'zjzak'
```
Turn multibase encoded string back into buffer

```python
>>> from stbx_hash import decode
>>> print(decode('zjzak').hex())
'7fff39'
```

**Note**: This does not seem to strip leading zery bytes from buffers such as `bytes([0,123]`

```python
zeropadded = bytes.fromhex('000000aabb')
print(decode(encode(zeropadded)).hex())
'aabb' # whoops we lost some zeros
```

To decode ASCII encoded strings, for example:

```python
>>> mb = 'zA9r2mGjF9pCtpHsXpUdPqPvmhR7jLvSnt'
>>> decode(mb).decode('ascii')
'decentralize everything!'
```

Encode them:

```python
>>> s = 'bla bla'
>>> encode(bytes(s,'ascii'))
'z4jL4YLu7MJ'
```

### hash : multibase -> multibase

1. Compute hash digest *h* of multibase encoded string.
2. Return a string that is the multibase-encoded multihash-wrapped hash digest *h*.


```python
>>> from stbx_hash import hash
>>> hash('zjzak')
'zFsGM26LeDFDhf3V8Np5GhyPoRVATEtd2oYKbaaXAZuh8'
>>> hash('zA9r2mGjF9pCtpHsXpUdPqPvmhR7jLvSnt')

```

### hashB : buffer -> buffer

compute hash digest of a buffer and return as a buffer

```python
>>> from stbx_hash import hash
>>> hash('zjzak')
'zFsGM26LeDFDhf3V8Np5GhyPoRVATEtd2oYKbaaXAZuh8'
```

## Installation

Make sure you have Python 3.6 or higher.

Dependencies (listed in `require.txt`)

- [multiformats/py-multihash](https://github.com/multiformats/py-multihash)
- [multiformats/py-multibase](https://github.com/multiformats/py-multibase)
- `protobuf`

To install the dependencies with the right version, run

```sh
pip install -r requirements-freeze.txt
```

To install the latest versions, run

```sh
pip install -r requirements.txt
```

Update the `requirements-freeze.txt` file

```sh
pip freeze > requirements-freeze.txt
```

### Virtual Environment

To isolate this installation from the main python system, you should use `virtualenv`.

1. Create a virtual env for this, in the directory `./venv`

```
# notice the "3"
virtualenv venv3 -p python3
```

2. activate the virtualenv with `source ./venv3/bin/activate.fish` (for [fish shell](https://fishshell.com/), see [virtualenv documentation here](https://virtualenv.pypa.io/en/latest/userguide/#activate-script) for more examples for other shells such as `bash`).

Now install the requirements (while in the environment)

```
# etc
pip install -r requirements-freeze.txt
```
### Rebuild the protocol buffer file

The `statebox.proto` file defines the transaction format; `statebox_pb2.py` is generated from it.

If you change `statebox.proto`, run the protocol buffer compiler to generate the `_pb2.py` file

```
protoc statebox.proto --python_out=statebox
```

