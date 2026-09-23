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
# ./cell05/ex12/string_are_arrays.py
# ./cell05/ex12/string_are_arrays.py "The character Z is not found in this string"
# ./cell05/ex12/string_are_arrays.py "The character z is found in this string"
# ./cell05/ex12/string_are_arrays.py "Zaz visits the zoo with Zazie"
