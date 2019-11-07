import sys

sys.stdin = open("./data/input.txt")

dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]
cleaner_dir_list = [
    [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
    ],
    [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
    ],
]
R, C, T = map(int, input().split())
result = 0
board_list = []
cleaner_point_list = []
for h in range(R):
    temp_list = list(map(int, input().split()))
    for w in range(C):
        if temp_list[w] == -1:
            cleaner_point_list.append((h, w))

    board_list.append(temp_list)
count = 0
while True:
    if count == T:
        break
    # 미세먼지 번식
    temp_dict = {}
    for h in range(R):
        for w in range(C):
            temp_count = 0
            if board_list[h][w] <= 0:
                continue
            for dh, dw in dir_list:
                nh = dh + h
                nw = dw + w
                if nh < 0 or nw < 0 or nh >= R or nw >= C or board_list[nh][nw] == -1:
                    continue
                if (nh, nw) not in temp_dict:
                    temp_dict[nh, nw] = 0
                temp_dict[nh, nw] += board_list[h][w] // 5
                temp_count += 1
            board_list[h][w] -= (board_list[h][w] // 5) * temp_count
    for h, w in temp_dict.keys():
        board_list[h][w] += temp_dict[h, w]
    # 청소기 돌리자
    for cleaner_idx in range(2):
        start_h, start_w = cleaner_point_list[cleaner_idx]
        h, w = start_h, start_w
        for dh, dw in cleaner_dir_list[cleaner_idx]:
            while True:
                nh = dh + h
                nw = dw + w
                if cleaner_idx == 0:
                    if nh > start_h:
                        break
                elif cleaner_idx == 1:
                    if nh < start_h:
                        break

                if nh < 0 or nw < 0 or nh >= R or nw >= C or board_list[nh][nw] == -1:
                    break
                if board_list[h][w] != -1:
                    board_list[h][w] = board_list[nh][nw]
                    board_list[nh][nw] = 0
                h = nh
                w = nw
    count += 1
result = 2
for board in board_list:
    result += sum(board)
print(result)
