#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# use input()function to read imput from keyboard
str1 = input("Please imput the first number:   ")
str2 = input("Please input the second number:   ")

#use int()function, this function is to convert string to integer
x = int(str1)
y = int(str2)

#print out result
print(x, "+", y, " = ", x+y)
print(x, "-", y, " = ", x-y)
print(x, "*", y, " = ", x*y)
print(x, "**", y, " = ", x**y)
print(x, "/", y, " = ", x/y)
print(x, "//", y, " = ", x//y)
print(x, "%", y, " = ", x%y)