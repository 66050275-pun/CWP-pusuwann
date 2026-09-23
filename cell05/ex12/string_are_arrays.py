#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    count = sys.argv[1].count("z")
    if count == 0:
        print("none")
    else:
        print("z" * count)

# Example test commands in terminal:
# ./string_are_arrays.py
# ./string_are_arrays.py "The character Z is not found in this string"
# ./string_are_arrays.py "The character z is found in this string"
# ./string_are_arrays.py "Zaz visits the zoo with Zazie"
