#!/usr/bin/python3
"""class  that inherits from list"""


class MyList(list):
    """class  that inherits from list"""

    def print_sorted(self):
        """list to append and sort the list"""
        sort_list = []

        for i in self:
            sort_list.append(i)
        sort_list.sort()
        print(sort_list)
