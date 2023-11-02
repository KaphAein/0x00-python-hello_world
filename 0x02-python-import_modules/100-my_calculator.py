#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys
    av = sys.argv
    count = len(av) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if av[2] == "+":
        print("{} {} {} = {}".format(int(av[1]), av[2], int(av[3]), (int(av[1]) + int(av[3]))))
    elif av[2] == "-":
        print("{} {} {} = {}".format(int(av[1]), av[2], int(av[3]), (int(av[1]) - int(av[3]))))
    elif av[2] == "*":
        print("{} {} {} = {}".format(int(av[1]), av[2], int(av[3]), (int(av[1]) * int(av[3]))))
    elif av[2] == "/":
        print("{} {} {} = {}".format(int(av[1]), av[2], int(av[3]), (int(av[1]) / int(av[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
