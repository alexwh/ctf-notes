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

for i in range(1,101):
    print(r.recvuntil("Find the next prime number after "))
    primeafter = int(r.recvuntil(":")[:-1])
    tosend = find_prime_range(primeafter+1, (primeafter+1)*2)
    r.sendline(tosend)
    log.info("prime after " + str(primeafter) + " is " + str(tosend))
    r.recvuntil("\n")
print(r.recvall())
