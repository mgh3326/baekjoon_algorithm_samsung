import sys

sys.stdin = open("./data/input.txt")


def find_board(_idx, _h, _w):
    if _idx == 0:
        return horizontal_board_list[_h - 1][_w - 1]
    if _idx == 1:
        return horizontal_board_list[_h][_w - 1]
    if _idx == 2:
        return vertical_board_list[_h - 1][_w - 1]
    if _idx == 3:
        return vertical_board_list[_h - 1][_w]


def dfs(current_h, current_w):
    if memo_list[current_h][current_w] != -1:
        return
    memo_list[current_h][current_w] = H
    for dir_idx in range(len(dir_list)):
        value = find_board(dir_idx, current_h, current_w)
        if value != -1:
            dh, dw = dir_list[dir_idx]
            nh, nw = dh + current_h, dw + current_w
            if memo_list[nh][nw] == -1:
                dfs(nh, nw)


dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]
N, M, H = map(int, input().split())
result = H * N * M
horizontal_board_list = [list(map(int, input().split())) for _ in range(M)]
vertical_board_list = [list(map(int, input().split())) for _ in range(N)]
memo_list = [[-1 for _ in range(M + 2)] for _ in range(N + 2)]
for h in range(N + 2):
    for w in range(M + 2):
        if h == 0 or w == 0 or h == N + 1 or w == M + 1:
            memo_list[h][w] = 0
for h in range(1, N + 1):
    for w in range(1, M + 1):
        dfs(h, w)
        print()

print(result)
