#!/usr/bin/env python3
import sys
from checkmate import checkmate
from board_chess import *

def main():
    # กระดานเริ่มต้น (สามารถเปลี่ยนกระดานทดสอบได้จากตรงนี้ หรือเรียกจาก board_chess ก็ได้)
    board = """\
R...
.K..
P.P.
....\
"""

    try:
        # หากมีการระบุชื่อไฟล์กระดานผ่าน Terminal (เช่น python3 main.py test.chess)
        if len(sys.argv) > 1:
            for filepath in sys.argv[1:]:
                with open(filepath, 'r') as f:
                    file_board = f.read()
                checkmate(file_board)
        else:
            # รันกระดานเริ่มต้น
            checkmate(board)
    except Exception:
        pass

if __name__ == "__main__":
    main()

# Example test commands in terminal:
# ./mini_project/ex00/main.py
