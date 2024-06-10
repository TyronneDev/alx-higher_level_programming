#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1 as calc

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, _, *, and /")
        exit(1)
    else:
        if argv[2] == '+':
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3],
                  calc.add(int(argv[1]), int(argv[3]))))
        elif argv[2] == '-':
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3],
                  calc.sub(int(argv[1]), int(argv[3]))))
        elif argv[2] == '*':
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3],
                  calc.mul(int(argv[1]), int(argv[3]))))
        elif argv[2] == '/':
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3],
                  calc.div(int(argv[1]), int(argv[3]))))
