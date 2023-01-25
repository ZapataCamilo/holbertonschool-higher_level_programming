#!/usr/bin/python3

i = 0
for i in range(0, 100):
    if i <= 98:
        print(f'{i:02d}, '.format(i + 1), end='')
    if i > 98:
        print(i, end='')
