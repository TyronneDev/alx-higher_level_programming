#!/usr/bin/python3
if __name__ == '__main__':
    from add_o import add

    a = 1
    b = 2
    sum = add(a+b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))
