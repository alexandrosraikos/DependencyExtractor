# Dependency Extractor

A Python library which extracts library dependencies from source files written in most mainstream programming languages.

## Usage

It is meant to be imported and called via a simple function, which returns an array of dependencies given single or multiple source files.

## Unit testing

To run unit tests using `unittest` on package modules, simply run:

`python -m unittest tests/test-analyze.py`

Please note that sample files from various programming languages in the `tests/data` directory will be used. These sample files contain simple applications.
