import sys

sys.stdin = open("input.txt")

rotate_list = [
    [3, 1, 0, 5, 4, 2],  # 동쪽으로 바꾸기
    [2, 1, 5, 0, 4, 3],  # 서쪽으로 바꾸기
    [4, 0, 2, 3, 5, 1],  # 북쪽으로 바꾸기
    [1, 5, 2, 3, 0, 4],  # 윗면이 앞쪽이 된다 (남쪽으로 바꾸기)
]
dice_list = [0] * 6
dir_list = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
]
N, M, h, w, K = map(int, input().split())
board_list = [list(map(int, input().split())) for i in range(N)]

# 항상 0이라서 필요가 없네
# value_list[-1] = board_list[h][w]
# board_list[h][w] = 0

result = 0
d_list = list(map(int, input().split()))
for _d in d_list:
    d = _d - 1
    dh, dw = dir_list[d]
    nh, nw = h + dh, w + dw
    if nh < 0 or nw < 0 or nh >= N or nw >= M:
        continue
    h, w = nh, nw
    # rotate
    dice_list_copy = dice_list.copy()
    for idx, value in enumerate(rotate_list[d]):
        dice_list[idx] = dice_list_copy[value]
    print(dice_list[0])
    if board_list[nh][nw] != 0:
        dice_list[-1] = board_list[nh][nw]
        board_list[nh][nw] = 0
    else:
        board_list[nh][nw] = dice_list[-1]
