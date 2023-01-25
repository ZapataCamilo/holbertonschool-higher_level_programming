#!/usr/bin/python3
abc = 97

for abc in range(97, 123):
    if abc == 101 or abc == 113:
        continue
    print(chr(abc).format(abc + 1), end='')
