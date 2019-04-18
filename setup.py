from setuptools import setup

# see for details:
# https://python-packaging.readthedocs.io/en/latest/minimal.html
setup(
    name='statebox',
    version='0.1.1',
    packages=['statebox'],
    install_requires=[
        'protobuf',
        'py-multibase',
        'py-multihash',
        'requests'
    ]
)