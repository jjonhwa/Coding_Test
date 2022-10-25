"""
문제
    1. *F -> F*
    2. *S -> S*
    3. F*이 하나라도 있을 경우, 가장 첫 곡은 F*. 없다면 무시.

문제풀이
    1. FS가 없고, FF만 있을 경우, FF count 후 종료
    2. 그 외
        1. FF 전부 사용
        2. FS -> SF 반복
        3. FS -> S* 이동
        4. SS 전부 사용
        5. SF 사용 후 종료
"""

import sys
input = sys.stdin.readline

FF, FS, SF, SS = list(map(int, input().split()))

total = 0

# 1. FS가 없고, FF만 있을 경우, FF count 후 종료
if FF and FS == 0:
    total = FF

else:
    # 1. FF 전부 사용
    count = FF
    FF -= count
    total += count

    # 2. FS -> SF 반복
    if FS:
        if FS <= SF:
            count = FS - 1
        else:
            count = SF
        
        FS -= count
        SF -= count
        total += count * 2

    # 3. FS -> S*로 이동
    if FS: # FS > SF일 경우, 한 번 추가 이동
        count = 1
        FS -= count
        total += 1

    # 4. SS 전부 사용
    count = SS
    SS -= count
    total += count

    # 5. SF 사용 후 종료
    if SF:
        count = 1
        SF -= count
        total += 1

print(total)