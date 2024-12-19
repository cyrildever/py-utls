# py-utls
_Utilities for Python_

![PyPI](https://img.shields.io/pypi/v/py-utls)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/cyrildever/py-utls)
![GitHub last commit](https://img.shields.io/github/last-commit/cyrildever/py-utls)
![GitHub issues](https://img.shields.io/github/issues/cyrildever/py-utls)
![GitHub](https://img.shields.io/github/license/cyrildever/py-utls)

`py-utls` is a small Python repository where I put all the useful stuff I regularly need in my projects. \
Feel free to use at your discretion with the appropriate license mentions.

_NB: I've developed the same kind of libraries for both [Go](https://github.com/cyrildever/go-utls) and [TypeScript](https://www.npmjs.com/package/ts-utls)._

### Usage

```console
pip install py-utls
```

This repository contains the following modules:
* `hex`:
  - `from_hex`: builds the byte array from a string;
  - `to_hex`: creates the hexadecimal representation of a byte array;
* `list`:
  - `chunk`: split a list into chunks of a maximum size;
  - `flatten`: transforms a list of list of items to a list of items;
* `number`:
  - `euclidean_division`: compute the euclidean division of the passed integers.


```python
from pyutls.hex import from_hex, to_hex
from pyutls.list import chunk, flatten
from pyutls.number import euclidean_division

# Hex utilities
barray = from_hex('1234abcd')
hex_string = to_hex(barray)
assertEqual(hex_string == '1234abcd')

# Flatten a list of list
chunks = chunk(some_list, size)
flat_list = flatten(chunks)
assertListEqual(flat_list == some_list)

# Euclidean division
quotient, remainder = euclidean_division(numerator, denominator)
assertEqual(quotient * denominator + remainder == numerator)
```


### Tests

```console
$ python3 -m unittest discover
```


### License

These modules are distributed under a MIT license. \
See the [LICENSE](LICENSE) file.


<hr />
&copy; 2022-2024 Cyril Dever. All rights reserved.