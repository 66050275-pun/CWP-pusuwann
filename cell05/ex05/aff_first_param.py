#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")

# Example test commands in terminal:
# ./aff_first_param.py
# ./aff_first_param.py "Code Ninja" "Numerique" "42"
