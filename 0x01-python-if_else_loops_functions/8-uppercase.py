#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i in range(97, 123):
            i = (ord(i)) - 32
        print("{:c}".format(i), end="")
        print()
