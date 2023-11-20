#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("{}".format(a/b))
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result:{}".format({}))
    return a/b
