#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    str = argv
    str_len = len(str)

    if str_len:
        if str_len == 1:
            print('0 arguments.')
        elif str_len == 2:
            print('{} argument:'.format(str_len - 1))
        elif str_len > 2:
            print('{} arguments:'.format(str_len - 1))
        for i in range(1, str_len):
            i == i + 1
            if str[i]:
                print('{}: {}'.format(i, str[i]))
    elif str[0]:
        print('{} arguments.'.format(str_len))
