# py-utls
_Utilities for Python_

![PyPI](https://img.shields.io/pypi/v/py-utls)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/cyrildever/py-utls)
![GitHub last commit](https://img.shields.io/github/last-commit/cyrildever/py-utls)
![GitHub issues](https://img.shields.io/github/issues/cyrildever/py-utls)
![GitHub](https://img.shields.io/github/license/cyrildever/py-utls)

py-utls is a small Python repository where I put all the useful stuff I regularly need in my projects.
Feel free to use at your discretion with the appropriate license mentions.

_NB: I've developed the same kind of libraries for both [Go](https://github.com/cyrildever/go-utls) and [TypeScript](https://www.npmjs.com/package/ts-utls)._

### Usage

```console
pip install py-utls
```

This repository contains the following modules:
* `list`:
  - `flatten`: transforms a list of list of items to a list of items.


```python
from pyutls.list import flatten

flat_list = flatten(list1, list2)
```


### License

These modules are distributed under a MIT license. \
See the [LICENSE](LICENSE) file.


<hr />
&copy; 2022 Cyril Dever. All rights reserved.