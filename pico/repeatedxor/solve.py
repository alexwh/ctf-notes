#!/usr/bin/env python3

def xor(input_data, key):
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result

def hamming_distance(a, b):
    # The Hamming distance of two words A and B can be calculated as the Hamming weight of A xor B.
    pass

with open("encrypted.raw", "rb") as file:
    input_data = file.read()

for i in range(1,256):
    pass
