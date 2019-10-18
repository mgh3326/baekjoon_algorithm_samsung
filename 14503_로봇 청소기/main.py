import sys

sys.stdin = open("./data/input.txt")

dir_list = [  # index가 커질수록 시계방향이네(오른쪽 방향)
    [-1, 0],  # 북
    [0, 1],  # 동
    [1, 0],  # 남
    [0, -1],  # 서
]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board_list = [list(map(int, input().split())) for i in range(N)]
result = 0
board_list[r][c] = 2
result += 1
h, w = r, c
while True:
    for dh, dw in dir_list:
        nh, nw = h + dh, w + dw
        if board_list[nh][nw] == 0:
            break
    else:  # 모두 벽이거나 청소 되어 있는칸
        nd = (d - 2) % 4  # 뒤쪽 방향
        dh, dw = dir_list[nd]
        nh, nw = h + dh, w + dw
        if board_list[nh][nw] == 1:  # 종료 (D 단계)
            break
        h, w = nh, nw  # (C 단계)
        continue

    nd = (d - 1) % 4  # 왼쪽 방향
    dh, dw = dir_list[nd]
    nh, nw = h + dh, w + dw
    d = nd
    if board_list[nh][nw] == 0:  # (A 단계)
        h, w = nh, nw
        board_list[nh][nw] = 2
        result += 1
        continue
    # (B 단계)
print(result)
