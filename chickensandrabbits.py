#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 35
b = 94

for x in range (1,a):
    y = a - x
    if 2 * x + 4 * y == b:
        print("chicken has " + str(x) + ", rabbits has " + str(y) + " is correct")
    else:
        continue
        # print("chicken has " + str(x) + ", rabbits has " + str(y) + " isn't correct")    