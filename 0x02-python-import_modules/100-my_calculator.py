#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys
    x = sys.argv
    count = len(x) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(x[1])
    b = int(x[3])

    if x[2] == "+":
        print("{} + {} = {}".format(a, b, a + b))
    elif x[2] == "-":
        print("{} - {} = {}".format(a, b, a - b))
    elif x[2] == "*":
        print("{} * {} = {}".format(a, b, a * b))
    elif x[2] == "/":
        print("{} / {} = {}".format(a, b, a / b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
