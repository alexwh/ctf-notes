#!/usr/bin/env python2
from pwn import *
import operator
class whatever:
    def _xor(self, charcode):
        return charcode ^ (2<<4)

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in xrange(0, len(l), n):
            yield l[i:i+n]

    def encode(self, eq):
        out = []
        for c in eq:
            q = bin(self._xor(ord(c))).lstrip("0b")
            q = "0" * ((2<<2)-len(q)) + q # padding
            out.append(q)
        print(out)
        b = ''.join(out)
        pr = []
        for x in range(0,len(b),2):
            c = chr(int(b[x:x+2],2)+51)
            pr.append(c)
        s = '.'.join(pr)
        return s

    def decode(self, string):
        pr = string.split(".")
        decoded = ""
        # one character is 4 numbers long
        for letter in self.chunks(pr,4):
            total = []
            for num in letter:
                # char code for 3 is 51, offset there
                result = bin(int(num) - 3).lstrip("0b")
                result = "0" * (2-len(result)) + result # padding
                total.append(result)
            total = "".join(total)
            total = chr(self._xor(int(total,2)))
            decoded += "".join(total)
        return decoded

yo = whatever()
mapper = {
	"+": operator.sub,
	"-": operator.add,
	"*": operator.div,
}

r = remote("188.166.133.53", 11071)
for i in range(1, 101):
    r.recvuntil(": ")
    string = r.recvuntil("\n").strip()
    decoded = yo.decode(string)
    print decoded
    split = decoded.split(" ")
    type = split[1]
    first = split[2]
    result = split[4]
    print type,first,result
    tosend = yo.encode(str(mapper[type](int(result), int(first))))
    print(tosend)
    r.sendline(tosend)
    print r.recvuntil("\n")
print(r.recv(1024))
