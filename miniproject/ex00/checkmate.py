#!/usr/bin/env python3

def print_grid(grid):
    print("[", end="")
    for i, row in enumerate(grid):
        if i == 0:
            print(f"{row},")
        elif i == len(grid) - 1:
            print(f" {row}]")
        else:
            print(f" {row},")

def checkmate(board):
    if not board or not isinstance(board, str):
        print("Error: Empty or invalid board.")
        return

    lines = [line.strip() for line in board.splitlines() if line.strip()]
    if not lines:
        print("Error: Empty board.")
        return

    num_rows = len(lines)
    for i, row in enumerate(lines):
        if len(row) != num_rows:
            print(f"Error: Invalid dimension (Board is not a square: {num_rows} rows x row {i+1} has {len(row)} cols).")
            return

    size = num_rows

    king_positions = []
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_positions.append((r, c))

    if len(king_positions) == 0:
        print("Error: No King found on the board.")
        return
    elif len(king_positions) > 1:
        print(f"Error: King unit exceeds limit (Found {len(king_positions)} Kings, must be exactly 1).")
        return

    kr, kc = king_positions[0]

    grid = [list(row) for row in lines]
    print_grid(grid)
    print(f"({size}, {size})")

    check_board = [list(row) for row in lines]

    def mark_attack(r, c):
        if check_board[r][c] in ('.', 'K'):
            check_board[r][c] = 'X'

    for r in range(size):
        for c in range(size):
            piece = lines[r][c]

            if piece == 'P':
                p_row = r - 1
                for p_col in (c - 1, c + 1):
                    if 0 <= p_row < size and 0 <= p_col < size:
                        mark_attack(p_row, p_col)

            if piece in ('R', 'Q'):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    cr, cc = r + dr, c + dc
                    while 0 <= cr < size and 0 <= cc < size:
                        mark_attack(cr, cc)
                        if lines[cr][cc] in ('P', 'B', 'R', 'Q', 'K'):
                            break
                        cr += dr
                        cc += dc

            if piece in ('B', 'Q'):
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    cr, cc = r + dr, c + dc
                    while 0 <= cr < size and 0 <= cc < size:
                        mark_attack(cr, cc)
                        if lines[cr][cc] in ('P', 'B', 'R', 'Q', 'K'):
                            break
                        cr += dr
                        cc += dc

    print("Check Range:")
    print_grid(check_board)

    if check_board[kr][kc] == 'X':
        print("Success")
    else:
        print("Fail")
