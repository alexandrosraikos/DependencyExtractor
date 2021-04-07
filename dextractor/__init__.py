# ---------
# This source file is part of the Dependency Extractor python open source package.
# Copyright (c) 2021, Alexandros Raikos tou Konstantinou.
#
# Licensed under the MIT License.
# ---------

from typing import Set
import os
import re

# Define supported languages with their corresponding compiled import regex.
known_expressions = {
    ".cpp": re.compile(r"#include [<\"](?P<dependency>[a-z]+)[\">]"),
}


def analyze(any_path: str, max_file_size=10000000) -> Set:
    """
    Retrieve any path and analyze its source file content for library dependencies.
    """

    def find_in(file_path: str) -> Set:
        """
        Read the source file and extract imported package names using regular expressions.
        """
        found = set()

        # 1. When file is written in a supported language.
        filename, extension = os.path.splitext(file_path)
        if extension in known_expressions:
            # 1.1. When file isn't too large.
            # -----
            # NOTE: Most source files for most use cases are not
            #       expected to exceed 10MB in size.
            if os.stat(file_path).st_size < max_file_size:
                try:
                    file = open(file_path, "r")

                    # TODO: Implement regex scan.
                    matches = known_expressions[extension].match(file.read())
                    found.add(matches.group("dependency"))

                    file.close()
                except IOError:
                    print(
                        f"""
                        -------------------- ERROR --------------------
                        There was an IO error when trying to access the
                        file '{filename}'.
                        -----------------------------------------------
                        """
                    )
            else:
                raise MemoryError(
                    f"""
                    -------------------- ERROR --------------------
                    The file '{filename}' is too large.
                    -----------------------------------------------
                    """
                )
        else:
            raise NotImplementedError(
                """
                    -------------------- ERROR --------------------
                    This programming language is currently not 
                    supported by this package.
                    -----------------------------------------------
                """
            )
        return found

    # 0. Initialise empty dependencies array.
    dependencies = set()

    # 1. Process given path.
    if os.path.isdir(any_path):
        # 1.1. When the given path points to a directory,
        # recursively check the directory tree for all files.
        for root, _, files in os.walk(any_path):
            for file in files:
                try:
                    dependencies.update(find_in(os.path.join(root, file)))
                except NotImplementedError:
                    print(
                        f"-- [dextractor] NOTICE: The file '{file}' is not yet supported by this module."
                    )
                except MemoryError:
                    print(f"-- [dextractor] NOTICE: The file '{file}' is too large.")
                except IOError:
                    print(
                        f"-- [dextractor] ERROR: The file '{file}' could not be accessed."
                    )

    elif os.path.isfile(any_path):
        # 1.2. When the given path points to a single file.
        # -----
        # NOTE: Exception descriptions are different when
        #       running the script for a single file.
        filename, extension = os.path.splitext(any_path)
        try:
            dependencies = dependencies.union(find_in(any_path))
        except NotImplementedError:
            print(
                f"-- [dextractor] ERROR: The file '{filename}{extension}' is not yet supported by this module."
            )
        except MemoryError:
            print(
                f"-- [dextractor] ERROR: The file '{filename}{extension}' is too large."
            )
        except IOError:
            print(
                f"-- [dextractor] ERROR: The file '{filename}{extension}' could not be accessed."
            )
    else:
        raise Exception(
            """
            -------------------- ERROR --------------------
            This is not a file or a directory. It might be 
            a special file (e.g. socket, FIFO, device file), 
            which is unsupported by this package.
            -----------------------------------------------
            """
        )

    return dependencies