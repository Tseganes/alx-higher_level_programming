#!/usr/bin/python3
'''
Write a function that appends a string
at the end of a text file (UTF8) and returns
the number of characters added
'''


def append_write(filename="", text=""):
    '''
    Append a string to the end of a UTF8 text file.
    Args:
         filename (str): The name of the file to append to.
         text (str): The string to append to the file.
    Return:
         The numbers of characters appended.
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        append_file = f.write(text)
        f.close()
        return append_file
