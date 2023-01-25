#!/usr/bin/python3

i = 0

for i in range(0, 100):
    if i >= 10:
        print(f'{i}, '.format(i + 1), end='')
    if i < 10:
        print(f'0{i}, '.format(i + 1), end='')
