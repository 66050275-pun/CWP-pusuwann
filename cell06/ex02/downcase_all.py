#!/usr/bin/env python3
import sys

def downcase_it(string):
    return string.lower()

if len(sys.argv) <= 1:
    print("none")
else:
    for param in sys.argv[1:]:
        print(downcase_it(param))

# Example test commands in terminal:
# ./cell06/ex02/downcase_all.py
# ./cell06/ex02/downcase_all.py "HELLO WORLD" "I understood Arrays well!"
