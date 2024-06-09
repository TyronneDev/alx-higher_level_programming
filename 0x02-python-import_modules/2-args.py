#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

   
    print("{:d} argument".format(len(argv) - 1), end="")
    if len(argv) - 1 == 0:
        print("s.")
    else:
        if len(argv) - 1 == 1:
            print(".")
        elif len(argv) - 1 > 1:
            print("s.")
        for idx in range(1, len(argv)):
            print("{}: {}".format(idx, argv[idx]))



