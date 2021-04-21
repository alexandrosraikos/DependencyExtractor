# ---------
# This source file is part of the Dependency Extractor python open source package.
# Copyright (c) 2021, Alexandros Raikos tou Konstantinou.
#
# Licensed under the MIT License.
# ---------

# Standard library.
import os
from os import name, path
from typing import Set

# Third party dependencies.
import colorama
from colorama import Fore

# Local package dependencies.
from .languages import supported_languages


class SourceFile:
    def __init__(self, path):
        """
        Retrieve any path and analyse all source file content for library dependencies.

        Parameters
        ----------
        - `path : str`
            A string containing the full system path for the source file.
        - `language : ProgrammingLanguage`
            A ProgrammingLanguage object which indicates the programming language of this source file.
        """
        if os.path.isfile(path):
            self.path: str = path
        else:
            raise TypeError
        self.name, self.extension = os.path.splitext(path)
        known = False
        for specific_language in supported_languages:
            if self.extension in specific_language.extensions:
                self.language = specific_language
                known = True
        if not known:
            raise NotImplementedError

    def dependencies(self, verbose: bool = False, strict: bool = False) -> Set:
        """
        Read the source file and extract imported package names using regular expressions.
        """
        # 0. Initialize empty set of discovered dependencies.
        found = set()

        # 1. When file is written in a supported language.
        # 1.1. When file isn't too large.
        # -----
        # NOTE: Most source files for most use cases are not
        #       expected to exceed 5MB in size (editable).
        try:
            # 1.1.1. Open file for reading.
            file = open(self.path, "r")
            if verbose:
                print("[dextractor]", end=" ")
                print(Fore.CYAN + "INFORMATION:", end=" ")
                print(f"Reading {os.path.basename(file.name)}")

            # 1.1.2. Match regex and obtain named capture group.
            if strict and ("strict" in self.language.expressions["dependencies"].keys()):
                query = self.language.expressions["dependencies"]["strict"]
            else:
                query = self.language.expressions["dependencies"]["regular"]
            matches = query.findall(file.read())
            found.update(matches)

            if not found and verbose:
                print("[dextractor]", end=" ")
                print(Fore.CYAN + "INFORMATION:", end=" ")
                print("This file doesn't include any dependencies.")
            # 1.1.3. Close file for memory optimisation.
            file.close()
        except IOError:
            print("[dextractor]", end=" ")
            print(Fore.RED + "ERROR:", end=" ")
            print(f"There was an IO error when trying to access the file '{name}'.")
        return found