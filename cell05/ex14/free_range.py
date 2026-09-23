#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    if start <= end:
        print(list(range(start, end + 1)))
    else:
        print(list(range(start, end - 1, -1)))

# Example test commands in terminal:
# ./cell05/ex14/free_range.py
# ./cell05/ex14/free_range.py 10 14
