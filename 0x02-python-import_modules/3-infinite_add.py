#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv
    count = len(av) - 1
    result = 0
    if count == 0:
        print("0")
    else:
        for i in range(count):
            result += int(av[i + 1])
    print("{}".format(result))
