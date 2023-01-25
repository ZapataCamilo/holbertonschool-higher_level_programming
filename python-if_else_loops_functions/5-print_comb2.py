#!/usr/bin/python3

i = 0

for i in range(0, 100):
    i + 1
    if i >= 10:
        print(i)
    if i < 10:
        print(f'0{i}')
