# Dependency Extractor

A Python library which extracts library dependencies from source files written in most mainstream programming languages.

## Getting started

Follow the steps below to get started with `dextractor`.

### Installation

This package can be install easily via `pip`. Run the commands below:

```bash
# Clone or download the .zip from the Releases tab.
git clone https://www.github.com/alexandrosraikos/dependency-extractor

# Navigate to the folder.
cd dependency-extractor

# Install locally
pip install .
```

### Usage

It is meant to be imported and called via a single module, which returns a `Set` of dependencies given a single file or a directory.

```python
from dextractor import analyse

# Use all default parameters.
dependencies = analyse("path/to/file/or/directory")

# Define a different maximum file size (in bytes).
dependencies = analyse("path/to/file/or/directory", max_file_size=2000000) # <- 2MB

# Ignore local and relative dependencies.
dependencies = analyse("path/to/file/or/directory", strict=True)

# Enable verbose output.
dependencies = analyse("path/to/file/or/directory", verbose=True)

```

## Unit testing

Please consult the README in the `tests` folder.

## Supported languages

All languages which are supported are still in alpha. Regular expressions which detect imports in source files must be polished and updated with the nuances of each programming language. Currently the supported languages are:

1. C/C++
1. Go
1. Python (_duh!_)
1. Java
