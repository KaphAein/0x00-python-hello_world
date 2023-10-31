#!/usr/bin/python3
for i in range(26, 0, -1):
    if(i % 2 == 0):
        c = chr(i + 96)
    elif(i % 2 != 0):
        c = chr(i + 64)
    print("{}".format(c), end="")
