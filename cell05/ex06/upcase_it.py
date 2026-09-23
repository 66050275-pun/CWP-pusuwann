#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")

# Example test commands in terminal:
# ./upcase_it.py
# ./upcase_it.py "initiation"
# ./upcase_it.py "This exercise is quite easy! "
