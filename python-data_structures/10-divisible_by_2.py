#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myList = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            myList.append(True)
        else:
            myList.append(False)
    return myList
