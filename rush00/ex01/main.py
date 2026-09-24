#!/usr/bin/env python3
import sys

def check_board_file(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = [line.rstrip('\r\n') for line in f if line.strip()]
    except Exception:
        print("Error")
        return

    if not lines:
        print("Error")
        return

    size = len(lines)
    for row in lines:
        if len(row) != size:
            print("Error")
            return

    king_pos = None
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                if king_pos is not None:
                    print("Error")
                    return
                king_pos = (r, c)

    if king_pos is None:
        print("Error")
        return

    kr, kc = king_pos

    pawn_row = kr + 1
    if pawn_row < size:
        for pawn_col in (kc - 1, kc + 1):
            if 0 <= pawn_col < size and lines[pawn_row][pawn_col] == 'P':
                print("Success")
                return

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ('R', 'Q'):
                print("Success")
                return
            elif piece in ('P', 'B', 'K'):
                break
            r += dr
            c += dc

    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ('B', 'Q'):
                print("Success")
                return
            elif piece in ('P', 'R', 'K'):
                break
            r += dr
            c += dc

    print("Fail")

def main():
    if len(sys.argv) < 2:
        return
    for arg in sys.argv[1:]:
        check_board_file(arg)

if __name__ == "__main__":
    main()
