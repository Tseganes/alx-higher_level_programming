#!/usr/bin/python3

"""Defines a file writing function."""

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Return:
       The numbers of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        file_write = f.write(text)
        f.close()
        return f.write(text)
