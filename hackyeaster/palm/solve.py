#!/usr/bin/env python3


"""if (u === 'elsa') {
    if (p > 0 && p.length == 10) {
        ok = true;
        for (i = 1; i <= 10; i++) {
            var digit = p.charAt(i - 1);
            var part = p.substring(0, i);
            if (used[digit] != 0 || part % i != 0) {
                ok = false
            }
            if (used[digit] == 0) {
                used[digit] = 1
            }
        }
    }
}"""

import itertools

base = "1234567890"
for i in itertools.permutations(base):
    i = "".join(i)
    ok = True
    for j in range(2,11):
        if int(str(i)[:j]) % j != 0:
            ok = False
            break
    if ok == True:
        print(i)
