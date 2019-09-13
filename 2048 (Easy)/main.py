import sys

sys.stdin = open("./data/input4.txt", "r")
import copy

dh = [-1, 0, 1, 0]  # 상 좌 하 우
dw = [0, -1, 0, 1]  # 상 좌 하 우
result = 0
board_size = int(input())
board_list = []
board_dict = {}
queue = []
board_set = set()
for i in range(board_size):
    temp_list = list(map(int, input().split()))
    for j in range(board_size):
        temp_value = temp_list[j]
        if temp_value != 0:
            if temp_value > result:
                result = temp_value
            board_dict[(i, j)] = temp_value
    board_list.append(temp_list)
board_set.add(tuple(board_list))

queue.append([board_dict.copy(), 0])
# TODO 더 효율적으로 짤수 없을까? 효율적으로 짜면, 문제도 맞춰질것 같다.
while True:
    if len(queue) == 0:
        break
    board_dict, depth = queue.pop(0)
    board_list = [[0 for x in range(board_size)] for y in range(board_size)]
    while True:
        if len(board_dict) == 0:
            break
        (h, w), value = board_dict.popitem()
        board_list[h][w] = value
    for dir_idx in range(len(dh)):
        nh = dh[dir_idx]
        nw = dw[dir_idx]
        temp_dict = {}
        temp_list = copy.deepcopy(board_list)
        if dir_idx == 0:
            for w in range(board_size):
                h = 0
                while True:
                    if h == board_size:
                        break
                    is_all_zero = True
                    if temp_list[h][w] == 0:
                        for i in range(board_size)[h + 1:]:
                            if temp_list[i][w] > 0:
                                temp_list[h][w] = temp_list[i][w]
                                temp_list[i][w] = 0
                                is_all_zero = False
                                break
                        if is_all_zero:
                            break
                    else:
                        for i in range(board_size)[h + 1:]:
                            if temp_list[i][w] > 0:
                                if temp_list[h][w] == temp_list[i][w]:
                                    temp_list[h][w] *= 2
                                    if temp_list[h][w] > result:
                                        result = temp_list[h][w]
                                    temp_dict[h, w] = temp_list[h][w]

                                    temp_list[i][w] = 0
                                    is_all_zero = False
                                    h += 1
                                    break
                                else:
                                    temp_dict[h, w] = temp_list[h][w]
                                    h += 1
                                    is_all_zero = False
                                    break
                        if is_all_zero:
                            temp_dict[h, w] = temp_list[h][w]

                            break
        elif dir_idx == 1:
            for h in range(board_size):
                w = 0
                while True:
                    if w == board_size:
                        break
                    is_all_zero = True
                    if temp_list[h][w] == 0:
                        for j in range(board_size)[w + 1:]:
                            if temp_list[h][j] > 0:
                                temp_list[h][w] = temp_list[h][j]
                                temp_list[h][j] = 0
                                is_all_zero = False
                                break
                        if is_all_zero:
                            break
                    else:
                        for j in range(board_size)[w + 1:]:
                            if temp_list[h][j] > 0:
                                if temp_list[h][w] == temp_list[h][j]:
                                    temp_list[h][w] *= 2
                                    if temp_list[h][w] > result:
                                        result = temp_list[h][w]
                                    temp_dict[h, w] = temp_list[h][w]
                                    temp_list[h][j] = 0
                                    is_all_zero = False
                                    w += 1
                                    break
                                else:
                                    temp_dict[h, w] = temp_list[h][w]
                                    is_all_zero = False

                                    w += 1
                                    break
                        if is_all_zero:
                            temp_dict[h, w] = temp_list[h][w]

                            break
        elif dir_idx == 2:
            for w in range(board_size):
                h = 0
                while True:
                    if h == board_size:
                        break
                    is_all_zero = True
                    if temp_list[board_size - 1 - h][w] == 0:
                        for i in range(board_size)[h + 1:]:
                            if temp_list[board_size - 1 - i][w] > 0:
                                temp_list[board_size - 1 - h][w] = temp_list[board_size - 1 - i][w]
                                temp_list[board_size - 1 - i][w] = 0
                                is_all_zero = False
                                break
                        if is_all_zero:
                            break
                    else:
                        for i in range(board_size)[h + 1:]:
                            if temp_list[board_size - 1 - i][w] > 0:
                                if temp_list[board_size - 1 - h][w] == temp_list[board_size - 1 - i][w]:
                                    temp_list[board_size - 1 - h][w] *= 2
                                    if temp_list[board_size - 1 - h][w] > result:
                                        result = temp_list[board_size - 1 - h][w]
                                    temp_dict[board_size - 1 - h, w] = temp_list[board_size - 1 - h][w]

                                    temp_list[board_size - 1 - i][w] = 0
                                    is_all_zero = False
                                    h += 1
                                    break
                                else:
                                    temp_dict[board_size - 1 - h, w] = temp_list[board_size - 1 - h][w]
                                    h += 1
                                    is_all_zero = False
                                    break
                        if is_all_zero:
                            temp_dict[board_size - 1 - h, w] = temp_list[board_size - 1 - h][w]
                            break
        elif dir_idx == 3:
            for h in range(board_size):
                w = 0
                while True:
                    if w == board_size:
                        break
                    is_all_zero = True
                    if temp_list[h][board_size - 1 - w] == 0:
                        for j in range(board_size)[w + 1:]:
                            if temp_list[h][board_size - 1 - j] > 0:
                                temp_list[h][board_size - 1 - w] = temp_list[h][board_size - 1 - j]
                                temp_list[h][board_size - 1 - j] = 0
                                is_all_zero = False
                                break
                        if is_all_zero:
                            break
                    else:
                        for j in range(board_size)[w + 1:]:
                            if temp_list[h][board_size - 1 - j] > 0:
                                if temp_list[h][board_size - 1 - w] == temp_list[h][board_size - 1 - j]:
                                    temp_list[h][board_size - 1 - w] *= 2
                                    if temp_list[h][board_size - 1 - w] > result:
                                        result = temp_list[h][board_size - 1 - w]
                                    temp_dict[h, board_size - 1 - w] = temp_list[h][board_size - 1 - w]

                                    temp_list[h][board_size - 1 - j] = 0
                                    is_all_zero = False
                                    w += 1
                                    break
                                else:
                                    temp_dict[h, board_size - 1 - w] = temp_list[h][board_size - 1 - w]
                                    is_all_zero = False
                                    w += 1
                                    break
                        if is_all_zero:
                            temp_dict[h, board_size - 1 - w] = temp_list[h][board_size - 1 - w]

                            break
        if depth < 5:
            queue.append([temp_dict, depth + 1])

print(result)
