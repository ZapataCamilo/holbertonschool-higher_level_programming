#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_myList = []
    for i in my_list:
        if i == search:
            i = replace
        new_myList.append(i)
    return new_myList
