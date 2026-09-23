#!/usr/bin/env python3

num_str = input("Give me a number: ")
try:
    val = float(num_str)
    if val.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("This number is a decimal.")
