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

known = {
    # C and C++
    ".cpp": re.compile(
        r"#include [<\"](?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+)[\">]"
    ),
    ".cpp-strict": re.compile(
        r"#include [<\"](?P<dependency>[^.][a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+[^.hpp][^.h])[\">]"
    ),
    ".hpp": re.compile(
        r"#include [<\"](?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+)[\">]"
    ),
    ".hpp-strict": re.compile(
        r"#include [<\"](?P<dependency>[^.][a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+[^.hpp][^.h])[\">]"
    ),
    ".c": re.compile(
        r"#include [<\"](?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+)[\">]"
    ),
    ".c-strict": re.compile(
        r"#include [<\"](?P<dependency>[^.][a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+[^.hpp][^.h])[\">]"
    ),
    ".h": re.compile(
        r"#include [<\"](?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+)[\">]"
    ),
    ".h-strict": re.compile(
        r"#include [<\"](?P<dependency>[^.][a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+[^.hpp][^.h])[\">]"
    ),
    # Golang
    # TODO: #1 Needs improvement (it only reads last dependency in list + strict mode.)
    ".go": re.compile(
        r"import \(\n(?:\t\"(?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-\[\]{};':\"\\.\/?]+)\"[\n]+)+\)"
    ),
    ".go-strict": re.compile(
        r"import \(\n(?:\t\"(?P<dependency>[a-zA-Z0-9!@#$%^&*()_+\-\[\]{};':\"\\.\/?]+)\"[\n]+)+\)"
    ),
    # Java
    ".java": re.compile(
        r"import (?P<dependency>[a-zA-Z0-9!@#$%^&*_+\-\[\]{};':\"\\.\/?]+);"
    ),
    ".java-strict": re.compile(
        r"import (?P<dependency>[a-zA-Z0-9!@#$%^&*_+\-\[\]{};':\"\\.\/?]+);"
    ),
    # Python
    ".py": re.compile(
        r"^(?:[ ]|)+(?:import|from) (?P<dependency>[^_][a-zA-Z0-9!@#$%^&*()_+\-\[\]{}.;':\"\\\/?]+)"
    ),
    ".py-strict": re.compile(
        r"^(?:[ ]|)+(?:import|from) (?P<dependency>[^_.][a-zA-Z0-9!@#$%^&*()_+\-\[\]{};':\"\\\/?]+)"
    ),
    ".pyi": re.compile(
        r"^(?:[ ]|)+(?:import|from) (?P<dependency>[^_][a-zA-Z0-9!@#$%^&*()_+\-\[\]{}.;':\"\\\/?]+)"
    ),
    ".pyi-strict": re.compile(
        r"^(?:[ ]|)+(?:import|from) (?P<dependency>[^_.][a-zA-Z0-9!@#$%^&*()_+\-\[\]{};':\"\\\/?]+)"
    ),
}