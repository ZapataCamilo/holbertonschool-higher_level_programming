#!/usr/bin/python3

for i in range(0, 10):
    for f in range(1, 10):
        if i >= f:
            continue
        elif i == 8 and f == 9:
            print('{}{}'.format(i, f))
        else:
            print('{}{}, '.format(i, f), end='')
