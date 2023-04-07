#!/usr/bin/env python

from random import *
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
R = randint(0, (len(num) - 1))
G = randint(0, (len(num) - 1))
B = randint(0, (len(num) - 1))

color = f'#{num[R]}{num[G]}{num[B]}'
print("Your HEX color is:", color)
