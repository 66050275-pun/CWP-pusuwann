#!/usr/bin/env python3
import sys
from checkmate import checkmate
from board_chess import *

def main():
    board = """\
R...
.K..
P.P.
....\
"""

    try:
        if len(sys.argv) > 1:
            for filepath in sys.argv[1:]:
                with open(filepath, 'r') as f:
                    file_board = f.read()
                checkmate(file_board)
        else:
            checkmate(board)
    except Exception:
        pass

if __name__ == "__main__":
    main()
