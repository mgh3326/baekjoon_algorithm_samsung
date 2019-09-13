import sys

sys.stdin = open("./data/input1.txt", "r")

dh = [0, 1, 0, -1]  # 우 하 좌 상
dw = [1, 0, -1, 0]  # 우 하 좌 상

board_size = int(input())
board_list = [[0 for x in range(board_size)] for y in range(board_size)]
direct_change_list = []
snake_list = [[0, 0]]
apple_size = int(input())
for k in range(apple_size):
    h, w = (map(int, input().split()))
    board_list[h - 1][w - 1] = 1
dir_size = int(input())
for k in range(dir_size):
    time, direct = list(input().split())
    direct_change_list.append([int(time), direct])
current_time = 0
dir_idx = 0
while True:
    current_h, current_w = snake_list[-1]

    nh = dh[dir_idx]
    nw = dw[dir_idx]
    next_h = current_h + nh
    next_w = current_w + nw
    if next_h >= board_size or next_w >= board_size or next_w < 0 or next_h < 0:
        break

    if [next_h, next_w] in snake_list:
        break
    if board_list[next_h][next_w] == 1:  # 사과 발견
        board_list[next_h][next_w] = 0
    else:
        snake_list.pop(0)
    snake_list.append([next_h, next_w])
    current_time += 1
    if len(direct_change_list) > 0:
        if current_time == direct_change_list[0][0]:
            time, dir_value = direct_change_list.pop(0)
            if dir_value == "D":
                dir_idx = (dir_idx + 1) % 4
            else:
                dir_idx = (dir_idx - 1) % 4
print(current_time + 1)
