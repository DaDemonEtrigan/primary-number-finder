# -*- coding: utf-8 -*-
num = int(input("Enter a number: "))
tag = False


if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            tag = True
            break
if tag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
