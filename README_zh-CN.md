<div align="center">

[English](README.md) | 简体中文
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

Python 中最简单的方式用于自动安装和导入多个库。灵感来源于 R 中的 [`pacman`](https://www.rdocumentation.org/packages/pacman/versions/0.5.1)。

## 功能

- 🤖 自动检测 pip 库是否未安装
- 🚀 比手动检测和安装更快速
- 👶 简单易用，像婴儿一样轻松上手

## 最近更新
- `2024-11-27` 初次发布，支持安装单个包和多个包列表

## 安装

`pip install pkgman`

## 使用方法
只需两行代码安装并导入一堆库：
- 单个模块
    ```Python

    from pkgman import include
    include("numpy")
    ```

- 多个模块

    ```Python

    from pkgman import include
    include(["numpy", "pandas"])
    ```
然后，所有库都会被导入；如果未安装，将先安装再导入。

### 示例 1. 导入可能未安装的多个模块
例如，如果我们想要导入 `numpy` 和 `pandas`，但这些包可能尚未安装，请参见 [multiple.modules.py](./example/multiple.modules.py)。

输出将会是：
```Bash
[pkgman] Installing and importing ['numpy', 'pandas']...
[pkgman] 2 packages have been imported.
```

现在我们检查它们是否正确导入：
```Python

Empty DataFrame
Columns: []
Index: [] 5.4
```

成功！

### 示例 2. 导入单个模块
您也可以仅用于一个模块：

```Python
from pkgman import include
include("numpy")
```

## 许可证
MIT 许可证
