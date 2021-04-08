# Testing

This directory is populated at will when cloning the repository. It is recommended to clone a complex open source repository in this directory and run the tests.

# How to

To run unit tests using `unittest` on package modules:

1. Clone a repository into the `data` folder.
1. From this project's root, run: `python -m unittest tests/test-analyse.py`
1. The testing script will return all imports found in the source code of your chosen repository.
