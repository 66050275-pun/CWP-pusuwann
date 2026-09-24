#!/usr/bin/env python3
import sys
from checkmate import checkmate

def main():
    board = """\
R...
.K..
..P.
....\
"""
    try:
        # หากมีการส่งชื่อไฟล์กระดานเข้ามาทาง argument
        if len(sys.argv) > 1:
            for filepath in sys.argv[1:]:
                with open(filepath, 'r') as f:
                    file_board = f.read()
                checkmate(file_board)
        else:
            # รันกระดานเริ่มต้นตามโจทย์
            checkmate(board)
    except Exception:
        pass

if __name__ == "__main__":
    main()

# Example test commands in terminal:
# ./mini_project/ex00/main.py
