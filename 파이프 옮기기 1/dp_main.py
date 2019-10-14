import sys

sys.stdin = open("./data/input.txt")

dirs = [
    [0, -1],
    [-1, 0],
    [-1, -1],
]
status_list = [
    [0],  # 가로
    [1],  # 세로
    [0, 1],  # 대각선
]


def find_memo(current_h, current_w, current_status):
    if memo[current_h][current_w][current_status] != -1:
        return memo[current_h][current_w][current_status]
    memo[current_h][current_w][current_status] = 0
    for next_status in (status_list[current_status]):
        dh, dw = dirs[next_status]
        next_h = current_h + dh
        next_w = current_w + dw
        if next_w < 0 or next_h < 0:
            continue
        next_value = find_memo(next_h, next_w, next_status)
        memo[current_h][current_w][current_status] += next_value
    # 대각선을 추가
    for dh, dw in dirs:
        next_h = current_h + dh
        next_w = current_w + dw
        if next_w < 0 or next_h < 0:
            break
        if board_list[next_h][next_w] == 1:
            break
    else:
        memo[current_h][current_w][current_status] += find_memo(current_h - 1, current_w - 1, 2)

    return memo[current_h][current_w][current_status]


n = int(input())
board_list = []
result = 0
memo = []
for h in range(n):
    temp_list = []
    for i in range(n):
        temp_list.append([[-1] * 3])
    memo.append(temp_list)
    temp_list = list(map(int, input().split()))
    for w in range(len(temp_list)):
        if temp_list[w] == 1:
            for i in range(3):
                memo[h][w][i] = 0
    board_list.append(temp_list)
start_status = 0
start_point_h = 0
start_point_w = 1
memo[start_point_h][start_point_w][0] = 1
for i in range(3):
    find_memo(n - 1, n - 1, i)
result = sum(memo[n - 1][n - 1])
print(result)
