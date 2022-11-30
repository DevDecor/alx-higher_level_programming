#!/usr/bin/python3
def print_last_digit(digit):
    if digit < 0:
        digit = -digit
    print(digit % 10)
    return digit % 10
