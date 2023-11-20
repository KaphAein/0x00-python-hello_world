#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], int) and isinstance(my_list_2[i], int):
                result[i] = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("wrong type")
            pass
        except (IndexError):
            print("out of range")
            pass
        except (ZeroDivisionError):
            print("division by 0")
            pass
        finally:
            print("{}".format(result))
    return result
