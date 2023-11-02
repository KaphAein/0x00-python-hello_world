#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys
    a = sys.argv
    count = len(a) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if a[2] == "+":
        print("{} + {} = {}".format(a[1], a[3], (int(a[1]) + int(a[3]))))
    elif a[2] == "-":
        print("{} - {} = {}".format(a[1], a[3], (int(a[1]) - int(a[3]))))
    elif a[2] == "*":
        print("{} * {} = {}".format(a[1], a[3], (int(a[1]) * int(a[3]))))
    elif a[2] == "/":
        print("{} / {} = {}".format(a[1], a[3], (int(a[1]) / int(a[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
