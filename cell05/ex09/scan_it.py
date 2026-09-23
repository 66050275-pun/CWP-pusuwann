#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    matches = re.findall(re.escape(sys.argv[1]), sys.argv[2])
    if matches:
        print(len(matches))
    else:
        print("none")

# Example test commands in terminal:
# ./scan_it.py
# ./scan_it.py "the"
# ./scan_it.py "the" "the quick brown fox jumps over the lazy dog"
