#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            convert = str[i]
            convert = ord(convert)
            convert = convert-32
            convert = chr(convert)
            str = str[:i] + convert + str[i + 1:]
    print('{}'.format(str))
