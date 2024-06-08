#!/usr/bin/python3
def reverse_alphabets():
    for i in range(122, 96, -1):
        if i % 2 == 0:
            i = i
        elif i % 2 == 1:
            i = i - 32
        print("{:c}".format(i), end="")
