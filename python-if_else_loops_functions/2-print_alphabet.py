#!/usr/bin/python3
abc = 97

for abc in range(97, 123):
    print(chr(abc).format(abc + 1), end='')
