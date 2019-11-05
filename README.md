# py-licor
Python logging software for the Licor 840 CO2/H2O analyzer

## Dependencies

  * bs4 (beautifulsoup)
  * pyserial

## Python Versions

This software package is written for Python 3+.

## Installation

To install from PyPi:

```sh
$ pip install py-licor [--upgrade]
```

To install directly from GitHub:

```sh

$ pip install git+https://github.com/quant-aq/py-licor.git
```

You can also download and install from source:

```sh

python setup.py install
```

## Documentation

There isn't any real documentation yet...but for now, there are only a few commands:

To setup a connection:

```python

import licor

dev1 = licor.Licor840()

# set the port
dev1.port = "/dev/tty.USA19H142P1.1"

# begin the connection
dev1.connect()

# read a line
dev1.read()
```

A successfull read will return a dictionary with the data - if it fails, it will return an empty dictionary. At any point, you can reset the port and re-connect. You can also set the default timeout using the `timeout` attribute of the Licor840 class. That's it! All connections on made using baud=9600.