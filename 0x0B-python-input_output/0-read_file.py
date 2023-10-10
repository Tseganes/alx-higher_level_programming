#!/usr/bin/python3

"""Define text file reading function. """

def read_file(filename=""):
    """Print the cintents of a UTF8 text file to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
