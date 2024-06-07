#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = (ord(i)) - 32
        print("{:c}".format(i), end="")
    print()
