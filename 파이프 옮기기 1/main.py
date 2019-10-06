import sys

sys.stdin = open("./data/input.txt")

dh = [0, 1, 1]  # 우, 하, 우하(대각선)
dw = [1, 0, 1]  # 우, 하, 우하(대각선)
status_possible_dir_list = [
    [0, 2],  # 가로
    [1, 2],  # 세로
    [0, 1, 2]  # 대각선
]


def dfs(current_point_h, current_point_w, current_status):
    global result
    if current_point_h == n - 1 and current_point_w == n - 1:
        result += 1
        return
    for dir_idx in status_possible_dir_list[current_status]:
        next_point_h = current_point_h + dh[dir_idx]
        next_point_w = current_point_w + dw[dir_idx]
        if next_point_h >= n or next_point_w >= n or next_point_h < 0 or next_point_w < 0 or board_list[next_point_h][
            next_point_w] == 1:
            continue
        if dir_idx == 2:
            if board_list[current_point_h][next_point_w] == 1 or board_list[next_point_h][current_point_w] == 1:
                continue
        dfs(next_point_h, next_point_w, dir_idx)


n = int(input())
board_list = []
result = 0
for i in range(n):
    temp_list = list(map(int, input().split()))
    board_list.append(temp_list)
start_status = 0
start_point_h = 0
start_point_w = 1
dfs(start_point_h, start_point_w, start_status)
print(result)
