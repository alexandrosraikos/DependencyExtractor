# ---------
# This source file is part of the Dependency Extractor python open source package.
# Copyright (c) 2021, Alexandros Raikos tou Konstantinou.
#
# Licensed under the MIT License.
# ---------

# Standard library.
import os
from typing import Set

# Third party dependencies.
import colorama
from colorama import Fore

# Local dependencies.
from .src.parser import SourceFile
from .src.exclusions import ignored_files, ignored_extensions


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
    ignored_counter = 0

    # - 0.2 Initialise colorama.
    colorama.init(autoreset=True)

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
                    # 1.1.2. Check for supported language and size.
                    if os.stat(os.path.join(root, file)).st_size < max_file_size:
                        if (os.path.splitext(file)[0] not in ignored_files) and (
                            os.path.splitext(file)[1] not in ignored_extensions
                        ):
                            # 1.1.3. Extract dependencies.
                            source_file = SourceFile(os.path.join(root, file))
                            dependencies.update(
                                source_file.dependencies(verbose, strict)
                            )
                            coverage_counter += 1
                        else:
                            ignored_counter += 1
                            raise TypeError
                    else:
                        raise MemoryError
                except TypeError:
                    if verbose:
                        print("[dextractor]", end=" ")
                        print(Fore.YELLOW + "NOTICE:", end=" ")
                        print(f"The file '{file}' does not contain source code.")
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
                    print(f"The file '{file}' could not be accessed.")
            # 1.1.4 Update total file count.
            total_file_count += len(files)
        # 1.1.5. Extract statistics.
        if len(files) > 0 and coverage_counter > 0:
            print("[dextractor]", end=" ")
            print(Fore.GREEN + "SUCCESS:")
            print(
                f"""
                 - - - - - - -
                | Files detected under {round(max_file_size/1000000,1)}MB: {total_file_count}
                | Files scanned: {coverage_counter}
                | Non-source files ignored: {ignored_counter}
                | Unsupported files: {total_file_count-coverage_counter-ignored_counter}
                | Source file coverage: {round(coverage_counter/(total_file_count-ignored_counter),3)*100}%
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
            source_file = SourceFile(any_path)
            dependencies.update(source_file.dependencies(verbose, strict))
            # 1.1.2. Check for supported language and size.
            if os.stat(any_path).st_size < max_file_size:
                if (os.path.splitext(source_file)[0] not in ignored_files) and (
                    os.path.splitext(source_file)[1] not in ignored_extensions
                ):
                    # 1.1.3. Extract dependencies.
                    source_file = SourceFile(any_path)
                    dependencies.update(source_file.dependencies(verbose, strict))
                    coverage_counter += 1
                else:
                    ignored_counter += 1
                    raise TypeError
            else:
                raise MemoryError
        except TypeError:
            if verbose:
                print("[dextractor]", end=" ")
                print(Fore.RED + "ERROR:", end=" ")
                print(
                    f"The file '{os.path.basename(filename)}{extension}' is not a source file."
                )
        except NotImplementedError:
            if verbose:
                print("[dextractor]", end=" ")
                print(Fore.YELLOW + "NOTICE:", end=" ")
                print(
                    f"The file '{os.path.basename(filename)}{extension}' is not yet supported by this module."
                )
        except MemoryError:
            if verbose:
                print("[dextractor]", end=" ")
                print(Fore.RED + "ERROR:", end=" ")
                print(
                    f"The file '{os.path.basename(filename)}{extension}' is too large."
                )
        except IOError:
            if verbose:
                print("[dextractor]", end=" ")
                print(Fore.RED + "ERROR:", end=" ")
                print(
                    f"The file '{os.path.basename(filename)}{extension}' could not be accessed."
                )
    else:
        raise Exception(
            "This is not a file or a directory. It might be a special file (e.g. socket, FIFO, device file), which is unsupported by this package. "
        )

    return dependencies