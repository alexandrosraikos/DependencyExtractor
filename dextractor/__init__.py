import re
import os

def analyze(path):
    if isinstance(path, str):
        return True
    if isinstance(path, list):
        return False