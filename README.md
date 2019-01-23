# Statebox Transaction Encoder

## API

- `makeFiringTransaction(previousHash, executionHash, messageHex, transition)`

## Rebuild the protocol buffer file

The `statebox.proto` file defines the transaction format; `statebox_pb2.py` is generated from it.

If you change `statebox.proto`, run the protocol buffer compiler to generate the `_pb2.py` file

```
protoc statebox.proto --python_out=.
```

## Install dependencies

First, create a virtual env for this, in the directory `./venv`

```
virtualenv venv3 -p python3
```

Then activate the virtualenv ` source ./venv3/bin/activate.fish` (for [fish shell](https://fishshell.com/), see [virtualenv documentation here](https://virtualenv.pypa.io/en/latest/userguide/#activate-script) for details).

Now install the requirements

```
pip install -r requirements.txt
```

## Use it:

```python
import statebox

txHex = statebox.makeFiringTransaction("deadbeef", "feedc0de", "cafebabe", 0)
print(txHex) # => b'0a04deadbeef120e0a04feedc0de10001a04cafebabe'
```