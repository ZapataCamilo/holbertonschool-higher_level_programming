#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elments = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            elments += 1
    except TypeError:
        pass
    finally:
        print()
        return elments
