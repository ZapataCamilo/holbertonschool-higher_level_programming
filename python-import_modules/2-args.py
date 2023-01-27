#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    str = argv
    str_len = len(str)

    if str:
        if str == str[0]:
            print('0 arguments.'.format(str_len -1))
        if str[1]:
            print('{} arguments:'.format(str_len - 1))
        for i in range(1, str_len):
            i == i + 1
            if str[i]:
                print('{}: {}'.format(i, str[i]))
