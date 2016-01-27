#!/usr/bin/env python3

# this will never work


import curses

secretz = [(1, 2), (2, 3), (8, 13), (4, 29), (130, 191), (343, 397), (652, 691), (858, 1009),
           (689, 2039), (1184, 4099), (2027, 7001), (5119, 10009), (15165, 19997), (15340, 30013),
           (29303, 70009), (42873, 160009), (158045, 200009)]

def calc(num):
    for idx, (r, m) in enumerate(secretz[::-1]):
        if num % m == r:
            stdscr.addstr(idx, 0, "{} % {} = {}\n".format(num, m, r))
            stdscr.refresh()
        else:
            return False

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

try:
    for i in range(158045, 2**64, 200009):
        calc(i)
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()
