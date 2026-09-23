#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print("none")
else:
    for param in reversed(sys.argv[1:]):
        print(param)

# Example test commands in terminal:
# ./aff_rev_params.py
# ./aff_rev_params.py "coucou"
# ./aff_rev_params.py "Python" "piscine" "hello"
