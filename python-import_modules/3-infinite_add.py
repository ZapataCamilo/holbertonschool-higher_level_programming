#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    sum = argv
    result = 0
    str_sum = len(sum)
    if sum[0] == 1:
        print(0)
    for i in range(1, str_sum):
        result += int(sum[i])
    print(result)
