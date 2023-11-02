#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv

    if len(av) == 1:
        print("{} arguments.".format(len(av) - 1))
    elif len(av) == 2:
        print("{} argument:".format(len(av) - 1))
    else:
        print("{} arguments:".format(len(av) - 1))
    for i in range(len(av) - 1):
        print("{}: {}".format(i + 1, av[i + 1])
