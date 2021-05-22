# ---------
# This source file is part of the Dependency Extractor python open source package.
# Copyright (c) 2021, Alexandros Raikos tou Konstantinou.
#
# Licensed under the MIT License.
# ---------
#
# Define a list of known configuration files, file extensions and names to be ignored.

configuration_files = [
    "Dockerfile",
    "Makefile",
    "docker-compose.yml",
    "serverless.yaml",
    "serverless.yml"
]

ignored_files = [
    ".gitignore",
    ".DS_Store",
    "README",
    "LICENSE",
    "MAINTAINERS",
    "BUGS",
    "CONTRIBUTING",
    "CONTRIBUTORS",
    "AUTHORS",
    "PATENTS",
]

ignored_extensions = [
    ".png",
    ".ico",
    ".jpg",
    ".svg",
    ".tiff",
    ".yml",
    ".yaml",
    ".rst",
    ".json",
    ".xml",
    ".html",
    ".har",
    ".properties",
    ".plist",
    ".all",
    ".txt",
    ".doc",
    ".xls",
    ".ppt",
    ".docx",
    ".xlsx",
    ".pptx",
    ".csv",
    ".jmx",
    ".cmd",
    ".sh",
    ".mod",
    ".sum",
    ".tpl",
    ".npy",
    ".npz",
    ".ini",
    ".inc",
]