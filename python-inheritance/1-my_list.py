#!/usr/bin/python3
# class  that inherits from list


class MyList(list):
    # class  that inherits from list

    def print_sorted(self):
        self.sort_list = [1, 4, 2, 3, 5]
        self.sort_list.sort()
        print(self.sort_list)
