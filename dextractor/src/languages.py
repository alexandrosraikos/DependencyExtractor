# ---------
# This source file is part of the Dependency Extractor python open source package.
# Copyright (c) 2021, Alexandros Raikos tou Konstantinou.
#
# Licensed under the MIT License.
# ---------
#
# Define supported languages with their corresponding compiled import regex.
# -----
# NOTE: Strict suffix queries exclude local and relative imports.
# NOTE: These expressions were formulated with the help of https://regex101.com.

import re
from typing import List


class ProgrammingLanguage:
    def __init__(self, name, extensions, expressions):
        self.name: str = name
        self.extensions: List[str] = extensions
        self.expressions = expressions


supported_languages = [
    ProgrammingLanguage(
        "C++",
        extensions=[".cpp", ".hpp"],
        expressions={
            "dependencies": {
                "regular": re.compile(
                    r"#include [<\"](?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+)[\">]"
                ),
                "strict": re.compile(
                    r"#include [<\"](?P<dependency>[^.][a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+[^.hpp][^.h])[\">]"
                ),
            }
        },
    ),
    ProgrammingLanguage(
        "C",
        extensions=[".c", ".h"],
        expressions={
            "dependencies": {
                "regular": re.compile(
                    r"#include [<\"](?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+)[\">]"
                ),
                "strict": re.compile(
                    r"#include [<\"](?P<dependency>[^.][a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+[^.hpp][^.h])[\">]"
                ),
            }
        },
    ),
    # TODO: #1 Needs improvement (it only reads last dependency in list + strict mode.)
    ProgrammingLanguage(
        "Go",
        extensions=[".go"],
        expressions={
            "dependencies": {
                "regular": re.compile(
                    r"import \(\n(?:\t\"(?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-\[\]{};':\"\\.\/?]+)\"[\n]+)+\)"
                )
            }
        },
    ),
    ProgrammingLanguage(
        "Java",
        extensions=[".java"],
        expressions={
            "dependencies": {
                "regular": re.compile(
                    r"import (?P<dependency>[a-zA-Z0-9!@#$%^&*_+\-\[\]{};':\"\\.\/?]+);"
                )
            }
        },
    ),
    ProgrammingLanguage(
        "Python",
        extensions=[".py", ".pyi"],
        expressions={
            "dependencies": {
                "regular": re.compile(
                    r"^(?:[ ]|)+(?:import|from) (?P<dependency>[^_][a-zA-Z0-9!@#$%^&*()_+\-\[\]{}.;':\"\\\/?]+)"
                ),
                "strict": re.compile(
                    r"^(?:[ ]|)+(?:import|from) (?P<dependency>[^_.][a-zA-Z0-9!@#$%^&*()_+\-\[\]{};':\"\\\/?]+)"
                ),
            }
        },
    ),
    ProgrammingLanguage(
        "JavaScript",
        extensions=[".json"],
        expressions={
            "dependencies": {
                "regular": re.compile(
                    r"\"dependencies\":[ |]{(?:[\n| |\t]+\"(?P<dependency>[^_.][a-zA-Z0-9!@#$%^&*()_+\-\[\]{};'\"\\\/?]+)\":[ |][a-zA-Z0-9!@#$%^&*()_+\-\.,[\]{};'\"\\\/?]+)"
                )
            }
        },
    ),
]