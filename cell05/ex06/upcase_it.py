#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")

# Example test commands in terminal:
# ./cell05/ex06/upcase_it.py
# ./cell05/ex06/upcase_it.py "initiation"
# ./cell05/ex06/upcase_it.py "This exercise is quite easy! "
