# Dependency Extractor

A Python library which extracts library dependencies from source files written in most mainstream programming languages.

## Usage

It is meant to be imported and called via a simple function, which returns an array of dependencies given a single file or a directory.

```python
from dextractor import analyze

dependencies = analyze("path/to-a/repo")
```

## Unit testing

Please consult the README in the `tests` folder.
