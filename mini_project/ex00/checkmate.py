#!/usr/bin/env python3

def print_grid(grid):
    """ฟังก์ชันช่วยพิมพ์กระดาน 2D List ให้มีรูปแบบสวยงามเหมือนในรูป"""
    print("[", end="")
    for i, row in enumerate(grid):
        if i == 0:
            print(f"{row},")
        elif i == len(grid) - 1:
            print(f" {row}]")
        else:
            print(f" {row},")

def checkmate(board):
    # -------------------------------------------------------------
    # 1. ตรวจสอบว่ามีข้อมูลส่งเข้ามาหรือไม่
    # -------------------------------------------------------------
    if not board or not isinstance(board, str):
        print("Error: Empty or invalid board.")
        return

    # แยกกระดานออกเป็นแต่ละแถว (ตัดช่องว่างหัวท้ายของแต่ละบรรทัดออก)
    lines = [line.strip() for line in board.splitlines() if line.strip()]
    if not lines:
        print("Error: Empty board.")
        return

    # -------------------------------------------------------------
    # 2. ตรวจสอบมิติของกระดาน (Dimension Check)
    # กระดานต้องเป็นสี่เหลี่ยมจัตุรัสเสมอ (เช่น 3x3, 4x4, 8x8)
    # ถ้าแถวสั้นยาวไม่เท่ากัน หรือไม่สมมาตร จะแจ้งเตือนทันที
    # -------------------------------------------------------------
    num_rows = len(lines)
    for i, row in enumerate(lines):
        if len(row) != num_rows:
            print(f"Error: Invalid dimension (Board is not a square: {num_rows} rows x row {i+1} has {len(row)} cols).")
            return

    size = num_rows

    # -------------------------------------------------------------
    # 3. ตรวจสอบจำนวน King ('K') บนกระดาน
    # กฎของโจทย์: ต้องมี King เพียงตัวเดียวเท่านั้น
    # -------------------------------------------------------------
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

    # -------------------------------------------------------------
    # 4. แสดงกระดานเริ่มต้นแบบ 2D List และขนาดของกระดาน
    # รองรับทุกขนาดที่เป็นสี่เหลี่ยมจัตุรัส (3x3, 4x4, ฯลฯ)
    # -------------------------------------------------------------
    grid = [list(row) for row in lines]
    print_grid(grid)
    print(f"({size}, {size})")

    # -------------------------------------------------------------
    # 5. คำนวณ Check Range (กระดานจำลองแสดงพื้นที่ที่หมากศัตรูสามารถโจมตีได้)
    # -------------------------------------------------------------
    check_board = [list(row) for row in lines]

    def mark_attack(r, c):
        # เปลี่ยนเป็น 'X' เฉพาะช่องว่าง ('.') หรือช่องที่เป็น King ('K')
        # จะไม่ทับหมากศัตรูตัวอื่น เพื่อให้คงตำแหน่งหมากเดิมไว้
        if check_board[r][c] in ('.', 'K'):
            check_board[r][c] = 'X'

    for r in range(size):
        for c in range(size):
            piece = lines[r][c]

            # เบี้ย (Pawn: 'P'): โจมตีเฉียงขึ้น 1 ช่อง (r - 1)
            if piece == 'P':
                p_row = r - 1
                for p_col in (c - 1, c + 1):
                    if 0 <= p_row < size and 0 <= p_col < size:
                        mark_attack(p_row, p_col)

            # เรือ (Rook: 'R') หรือ ควีน (Queen: 'Q'): โจมตี 4 ทิศ (ขึ้น, ลง, ซ้าย, ขวา)
            if piece in ('R', 'Q'):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    cr, cc = r + dr, c + dc
                    while 0 <= cr < size and 0 <= cc < size:
                        mark_attack(cr, cc)
                        if lines[cr][cc] in ('P', 'B', 'R', 'Q', 'K'):
                            break
                        cr += dr
                        cc += dc

            # บิชอป (Bishop: 'B') หรือ ควีน (Queen: 'Q'): โจมตี 4 ทิศแนวทแยง
            if piece in ('B', 'Q'):
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    cr, cc = r + dr, c + dc
                    while 0 <= cr < size and 0 <= cc < size:
                        mark_attack(cr, cc)
                        if lines[cr][cc] in ('P', 'B', 'R', 'Q', 'K'):
                            break
                        cr += dr
                        cc += dc

    # -------------------------------------------------------------
    # 6. แสดงผล Check Range และสรุปผล Success / Fail
    # -------------------------------------------------------------
    print("Check Range:")
    print_grid(check_board)

    # ถ้าตำแหน่งของ King ('K') โดนเปลี่ยนเป็น 'X' แสดงว่าโดนรุก!
    if check_board[kr][kc] == 'X':
        print("Success")
    else:
        print("Fail")
