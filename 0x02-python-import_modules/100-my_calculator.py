#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(argv[1])
b = int(argv[3])
op = argv[2]
if op == "+":
    f = add
elif op == "-":
    f = sub
elif op == "*":
    f = mul
elif op == "/":
    f = div
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
if __name__ == "__main__":
    print("{} {} {} = {}".format(a, op, b, f(a, b)))
