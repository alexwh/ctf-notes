#!/usr/bin/env python2

import sys

"""
Daedalus Corporation encryption script.
"""

def xor(input_data, key):
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result

def encrypt(input_data, password):
    key = 0
    for ch in password:
        key ^= ((2 * ord(ch) + 3) & 0xff)

    return xor(input_data, key)

def decrypt(input_data, password):
    return encrypt(input_data, password)

def usage():
    print("Usage: %s [encrypt/decrypt] [in_file] [out_file] [password]" % sys.argv[0])
    exit()

def main():
    input_data = open("encrypted", 'r').read()
    result_data = ""

    # if sys.argv[1] == "encrypt":
    #     result_data = encrypt(input_data, sys.argv[4])
    # elif sys.argv[1] == "decrypt":
    #     result_data = decrypt(input_data, sys.argv[4])
    # else:
    #     usage()

    for i in range(0, 256):
        print i
        print xor(input_data, i)
        print
        print


main()
