#!/usr/bin/python3

for i in range(0, 10):
    for f in range(1, 10):
        if i >= f:
            continue
        else:
            print(f'{i}{f}, '.format(i, f), end='')
