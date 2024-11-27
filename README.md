<div align="center">

English | [简体中文](README_zh-CN.md)
![img](./example/static/banner.png)
# Package Man
<p>
  <!-- PyPI -->
  <a href="https://pypi.org/project/pkgman/">
    <img src="https://img.shields.io/pypi/v/pkgman"/></a>
  <!-- License -->
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/reycn/pkgman"/></a>
  <a href="https://t.me/pkgman">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white"/></a>
</p>

</div>

The easiest way of auto installing and importing many libraries in Python. Inspired by [`pacman`](https://www.rdocumentation.org/packages/pacman/versions/0.5.1) in R

## Features

- 🤖 Auto-detection if a pip library is not installed
- 🚀 A faster way than manual detection and installation
- 👶 Ease-of-use at the baby level

## Recent updates
- `2024-11-27` Initialized, supporting installing a single package and a list of packages

## Installation

`pip install pkgman`

## Usage
Install and import a bunch of libraries using two lines:
- A single module
    ```Python

    from pkgman import include
    include("numpy")
    ```

- Many modules

    ```Python

    from pkgman import include
    include(["numpy", "pandas"])
    ```
Then, all of them will be imported; and if not installed, installed and imported.

### Example 1. Import multiple modules that may not be installed
For example, if we want to import `numpy` and `pandas` but the package may not be installed, see [multiple.modules.py](./example/multiple.modules.py)

And the outputs will be:
```Bash
[pkgman] Installing and importing ['numpy', 'pandas']...
[pkgman] 2 packages have been imported.
```

Now we check if they are properly imported:
```Python

Empty DataFrame
Columns: []
Index: [] 5.4
```

Yes!

### Example 2. Import a single modeul
You can also use it for only one module:

```Python
from pkgman import include
include("numpy")
```

## License
MIT License