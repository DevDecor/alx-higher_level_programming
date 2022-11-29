#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = f"Last digit of {number} is {abs(number)%10} "
if number % 10 == 0:
    string = string + "and is 0"
elif (abs(number) % 10) > 5:
    string = string + "and is greater than 5"
else:
    string = string + "and is less than 6 and not 0"
print(string)
