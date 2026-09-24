#!/usr/bin/env python3

def checkmate(board):
    # ตรวจสอบว่ามีข้อมูลส่งเข้ามาและเป็นสตริงหรือไม่
    if not board or not isinstance(board, str):
        return

    # แยกกระดานออกเป็นแต่ละแถว (ตัดบรรทัดว่างออก)
    lines = [line for line in board.splitlines() if len(line) > 0]
    if not lines:
        return

    # ตรวจสอบขนาดของกระดานว่าต้องเป็นสี่เหลี่ยมจัตุรัส (กว้าง x ยาว เท่ากัน)
    size = len(lines)
    for row in lines:
        if len(row) != size:
            return

    # ค้นหาตำแหน่งของ King ('K') บนกระดาน
    king_pos = None
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                # หากเจอกษัตริย์มากกว่า 1 ตัว ถือว่ากระดานไม่ถูกต้อง
                if king_pos is not None:
                    return
                king_pos = (r, c)

    # หากไม่พบกษัตริย์เลย
    if king_pos is None:
        return

    kr, kc = king_pos

    # ---------------------------------------------------------
    # 1. ตรวจสอบการโจมตีจากเบี้ย (Pawn: 'P')
    # ตามโจทย์ เบี้ยจะกินเฉียงขึ้นข้างบน 1 ช่อง (row - 1)
    # ดังนั้น ตัวที่จะกิน King ได้ จะต้องอยู่แถวล่างลงไป 1 แถว (kr + 1)
    # ---------------------------------------------------------
    pawn_row = kr + 1
    if pawn_row < size:
        # เบี้ยต้องอยู่คอลัมน์ซ้าย (kc - 1) หรือขวา (kc + 1)
        for pawn_col in (kc - 1, kc + 1):
            if 0 <= pawn_col < size:
                if lines[pawn_row][pawn_col] == 'P':
                    print("Success")
                    return

    # ---------------------------------------------------------
    # 2. ตรวจสอบแนวนอนและแนวตั้ง (เรือ: 'R' หรือ ควีน: 'Q')
    # เดินตรวจ 4 ทิศทาง: ขึ้น (-1, 0), ลง (1, 0), ซ้าย (0, -1), ขวา (0, 1)
    # ---------------------------------------------------------
    orthogonal_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in orthogonal_directions:
        r = kr + dr
        c = kc + dc
        # เดินทีละช่องไปเรื่อยๆ จนกว่าจะสุดขอบกระดาน
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            # ถ้าเจอ R หรือ Q แสดงว่า King โดนโจมตี
            if piece in ('R', 'Q'):
                print("Success")
                return
            # ถ้าเจอหมากตัวอื่น (P, B, K) ขวางทางไว้ ให้หยุดตรวจทิศนี้
            elif piece in ('P', 'B', 'K'):
                break
            # ถ้าเป็นช่องว่าง ('.') ให้เดินต่อไป
            r += dr
            c += dc

    # ---------------------------------------------------------
    # 3. ตรวจสอบแนวทแยง (บิชอป: 'B' หรือ ควีน: 'Q')
    # เดินตรวจ 4 ทิศทางทแยง: ทแยงซ้ายบน, ทแยงขวาบน, ทแยงซ้ายล่าง, ทแยงขวาล่าง
    # ---------------------------------------------------------
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        r = kr + dr
        c = kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            # ถ้าเจอ B หรือ Q แสดงว่า King โดนโจมตี
            if piece in ('B', 'Q'):
                print("Success")
                return
            # ถ้าเจอหมากตัวอื่น (P, R, K) ขวางทางไว้ ให้หยุดตรวจทิศนี้
            elif piece in ('P', 'R', 'K'):
                break
            # ถ้าเป็นช่องว่าง ('.') ให้เดินต่อไป
            r += dr
            c += dc

    # หากตรวจครบทุกทิศทางแล้ว ไม่มีหมากตัวใดโจมตี King ได้เลย
    print("Fail")
