#!/usr/bin/env python2

from pwn import *
r = remote("188.166.133.53", 11059)

def find_prime_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return str(p)
    return None

r.recvline() # welcome
while True:
    output = r.recvline()
    if "IW" in output:
        break
    print(output)
    # Level 1.: Find the next prime number after 9:
    primeafter = int(output.split()[-1][:-1])
    print(primeafter)
    tosend = find_prime_range(primeafter+1, (primeafter+1)*2)
    r.sendline(tosend)
    log.info("prime after " + str(primeafter) + " is " + str(tosend))
    print(r.recvline())
print(output)
