#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum = 0
    if len(argv) - 1 < 1:
        sum = 0
        print(sum)
    else:
        args = int(argv[1:])
        sum = 0
        for i in args:
            sum += i
        print(sum)
