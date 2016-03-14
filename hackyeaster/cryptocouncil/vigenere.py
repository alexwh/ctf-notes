#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt
import operator
from string import ascii_uppercase, ascii_lowercase

def caesar(message, shift=3):
    lower_table = str.maketrans(ascii_lowercase, ascii_lowercase[shift:] + ascii_lowercase[:shift])
    upper_table = str.maketrans(ascii_uppercase, ascii_uppercase[shift:] + ascii_uppercase[:shift])

    table = {**lower_table, **upper_table}
    return message.translate(table)

with open("text3") as f:
    text = f.read()

keylength = 5 # play with this
frequency = []

for i in range(keylength):
    count = {letter:0 for letter in ascii_uppercase}
    for letter in text[i::keylength]:
        if letter != '\n' and letter != ' ':
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    frequency.append(count)

for i, dic in enumerate(frequency):
    ax = sns.barplot(*zip(*sorted(dic.items(), key=operator.itemgetter(0))))
    plt.savefig("{}.png".format(i))
    plt.cla()


key = "PARIS"
output = ""

for i, letter in enumerate(text.replace(" ", "")):
    key_pos = key[i%keylength]
    distance = (ord("A") - ord(key_pos)) % 26
    output += caesar(letter, distance)

print(output)
