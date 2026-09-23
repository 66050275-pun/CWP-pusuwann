#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    print(sys.argv[1].lower())
else:
    print("none")

# Example test commands in terminal:
# ./cell05/ex07/downcase_it.py
# ./cell05/ex07/downcase_it.py "LUCIOLE"
# ./cell05/ex07/downcase_it.py "This exercise is quite easy! "
