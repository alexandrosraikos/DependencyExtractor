# ---------
# This source file is part of the Dependency Extractor python open source package.
# Copyright (c) 2021, Alexandros Raikos tou Konstantinou.
#
# Licensed under the MIT License.
# ---------

# Standard library.
import os
from typing import Set

# Third party deependencies.
import colorama
from colorama import Fore

# Local dependencies.
from .expressions import known

def analyse(
    any_path: str,
    max_file_size=5000000,
    strict=False,
    verbose=False,
) -> Set:
    """
    Retrieve any path and analyse all source file content for library dependencies.

    Parameters
    ----------
    - `any_path : str`
        A string containing a valid system path which is accessible from this script.
    - `max_file_size : int`
        A integer indicating the byte limit of source files to be read.
        This is useful for directories were irrelevant large data sets are also included.
    - `strict : bool`
        A flag which excludes internal and relative packages.
    - `verbose : bool`
        Enables verbose output for each scanned file.
    """

    # 0. Setup
    # - 0.1. Directory coverage counter.
    coverage_counter = 0

    # - 0.2 Initialise colorama
    colorama.init(autoreset=True)

    # - 0.3. Single file dependency analysis module.
    def find_in(file_path: str) -> Set:
        """
        Read the source file and extract imported package names using regular expressions.
        """
        # 0. Initialize empty set of discovered dependencies.
        found = set()
        nonlocal coverage_counter
        nonlocal strict
        nonlocal verbose

        # 1. When file is written in a supported language.
        filename, extension = os.path.splitext(file_path)
        if extension in known:
            # 1.1. When file isn't too large.
            # -----
            # NOTE: Most source files for most use cases are not
            #       expected to exceed 5MB in size (editable).
            if os.stat(file_path).st_size < max_file_size:
                try:
                    # 1.1.1. Open file for reading.
                    file = open(file_path, "r")
                    if verbose:
                        print("[dextractor]", end=" ")
                        print(Fore.CYAN + "INFORMATION:", end=" ")
                        print(f"Reading {os.path.basename(file.name)}")

                    # 1.1.2. Match regex and obtain named capture group.
                    if strict:
                        query = known[extension + "-strict"]
                    else:
                        query = known[extension]
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
                    print(
                        f"There was an IO error when trying to access the file '{filename}'."
                    )
            else:
                raise MemoryError()
        else:
            raise NotImplementedError()
        # 2. Increment directory coverage counter and return list of found dependencies.
        coverage_counter += 1
        return found

    # 0. Initialise empty dependencies array.
    dependencies = set()

    # 1. Process given path.
    if os.path.isdir(any_path):
        total_file_count = 0
        # 1.1. When the given path points to a directory,
        # recursively check the directory tree for all files.
        for root, _, files in os.walk(any_path):
            # 1.1.1. Traverse all available files.
            for file in files:
                try:
                    dependencies.update(find_in(os.path.join(root, file)))
                except NotImplementedError:
                    if verbose:
                        print("[dextractor]", end=" ")
                        print(Fore.YELLOW + "NOTICE:", end=" ")
                        print(f"The file '{file}' is not yet supported by this module.")
                except MemoryError:
                    if verbose:
                        print("[dextractor]", end=" ")
                        print(Fore.YELLOW + "NOTICE:", end=" ")
                        print(f"The file '{file}' is too large and will be ignored.")
                except IOError:
                    print("[dextractor]", end=" ")
                    print(Fore.RED + "ERROR:", end=" ")
                    print(
                        f"The file '{file}' could not be accessed."
                    )
            # 1.1.2 Update total file count.
            total_file_count += len(files)
        # 1.1.3. Extract statistics.
        if len(files) > 0 and coverage_counter > 0:
            print("[dextractor]", end=" ")
            print(Fore.GREEN + "SUCCESS:")
            print(
                f"""
                 - - - - - - -
                | Files detected under {round(max_file_size/1000000,1)}MB: {total_file_count}
                | Files scanned: {coverage_counter}
                | Scan coverage: {round(coverage_counter/total_file_count,3)*100}%
                | Dependencies found: {len(dependencies)}
                 - - - - - - -
                """
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
                if verbose:
                    print("[dextractor]", end=" ")
                    print(Fore.YELLOW + "NOTICE:", end=" ")
                    print(f"The file '{os.path.basename(filename)}{extension}' is not yet supported by this module.")
        except MemoryError:
                if verbose:
                    print("[dextractor]", end=" ")
                    print(Fore.RED + "ERROR:", end=" ")
                    print(f"The file '{os.path.basename(filename)}{extension}' is too large.")
        except IOError:
                if verbose:
                    print("[dextractor]", end=" ")
                    print(Fore.RED + "ERROR:", end=" ")
                    print(f"The file '{os.path.basename(filename)}{extension}' could not be accessed.")
    else:
        raise Exception(
            "This is not a file or a directory. It might be a special file (e.g. socket, FIFO, device file), which is unsupported by this package. "
        )

    return dependencies