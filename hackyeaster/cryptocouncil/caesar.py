#!/usr/bin/env python3

from string import ascii_uppercase, ascii_lowercase

def caesar(message, shift=3):
    lower_table = str.maketrans(ascii_lowercase, ascii_lowercase[shift:] + ascii_lowercase[:shift])
    upper_table = str.maketrans(ascii_uppercase, ascii_uppercase[shift:] + ascii_uppercase[:shift])

    table = {**lower_table, **upper_table}
    return message.translate(table)

with open("text1") as f:
    text = f.read()

for i in range(1, 26):
    print(i, caesar(text, i))
