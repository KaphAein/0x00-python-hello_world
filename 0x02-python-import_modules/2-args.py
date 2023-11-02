#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) > 1:
        print("{} arguments:".format(len(argv) - 1))
        for i < len(argv) - 1:
            print("{}: {}".format(i + 1, argv[i + 1])
