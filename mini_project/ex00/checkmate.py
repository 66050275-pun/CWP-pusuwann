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
    # ตรวจสอบว่ามีข้อมูลส่งเข้ามาและเป็นสตริงหรือไม่
    if not board or not isinstance(board, str):
        return

    # แยกกระดานออกเป็นแต่ละแถว
    lines = [line.strip() for line in board.splitlines() if line.strip()]
    if not lines:
        return

    size = len(lines)
    # ตรวจสอบขนาดกระดานว่าต้องเป็นสี่เหลี่ยมจัตุรัส (ความกว้าง = ความยาว)
    for row in lines:
        if len(row) != size:
            return

    # ค้นหาตำแหน่งของ King ('K')
    king_pos = None
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                if king_pos is not None:
                    return  # มี King มากกว่า 1 ตัว ถือว่ากระดานไม่ถูกต้อง
                king_pos = (r, c)

    if king_pos is None:
        return  # ไม่พบ King

    kr, kc = king_pos

    # 1. แสดงกระดานเริ่มต้นแบบ 2D List
    grid = [list(row) for row in lines]
    print_grid(grid)

    # 2. แสดงขนาดกระดาน (แถว, หลัก)
    print(f"({size}, {size})")

    # 3. คำนวณ Check Range (กระดานจำลองแสดงพื้นที่ที่หมากศัตรูสามารถโจมตีได้)
    check_board = [list(row) for row in lines]

    def mark_attack(r, c):
        # เปลี่ยนเป็น 'X' เฉพาะช่องว่าง ('.') หรือช่องที่เป็น King ('K')
        # จะไม่ทับหมากตัวอื่น เพื่อให้เห็นหมากศัตรูเดิม
        if check_board[r][c] in ('.', 'K'):
            check_board[r][c] = 'X'

    for r in range(size):
        for c in range(size):
            piece = lines[r][c]

            # --------------------------------------------------
            # เบี้ย (Pawn: 'P'): โจมตีเฉียงขึ้น 1 ช่อง (r - 1)
            # --------------------------------------------------
            if piece == 'P':
                p_row = r - 1
                for p_col in (c - 1, c + 1):
                    if 0 <= p_row < size and 0 <= p_col < size:
                        mark_attack(p_row, p_col)

            # --------------------------------------------------
            # เรือ (Rook: 'R') หรือ ควีน (Queen: 'Q'): โจมตี 4 ทิศ (ขึ้น, ลง, ซ้าย, ขวา)
            # --------------------------------------------------
            if piece in ('R', 'Q'):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    cr, cc = r + dr, c + dc
                    while 0 <= cr < size and 0 <= cc < size:
                        mark_attack(cr, cc)
                        # หากเจอหมากตัวอื่นขวางทางไว้ ให้หยุดเดินในทิศนี้
                        if lines[cr][cc] in ('P', 'B', 'R', 'Q', 'K'):
                            break
                        cr += dr
                        cc += dc

            # --------------------------------------------------
            # บิชอป (Bishop: 'B') หรือ ควีน (Queen: 'Q'): โจมตี 4 ทิศแนวทแยง
            # --------------------------------------------------
            if piece in ('B', 'Q'):
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    cr, cc = r + dr, c + dc
                    while 0 <= cr < size and 0 <= cc < size:
                        mark_attack(cr, cc)
                        # หากเจอหมากตัวอื่นขวางทางไว้ ให้หยุดเดินในทิศนี้
                        if lines[cr][cc] in ('P', 'B', 'R', 'Q', 'K'):
                            break
                        cr += dr
                        cc += dc

    # 4. แสดง Check Range
    print("Check Range:")
    print_grid(check_board)

    # 5. สรุปผล: ถ้าตำแหน่งของ King ('K') ถูกเปลี่ยนเป็น 'X' แสดงว่าโดนรุก!
    if check_board[kr][kc] == 'X':
        print("Success")
    else:
        print("Fail")
