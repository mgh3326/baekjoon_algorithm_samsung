import sys

sys.stdin = open("input.txt")

import heapq

r, c, k = map(int, input().split())
r -= 1
c -= 1
result = -1
h_count = 3
w_count = 3
board_list = []
for h in range(200):
    temp_list = [-1] * 200
    board_list.append(temp_list)
for h in range(h_count):
    temp_list = list(map(int, input().split()))
    for w in range(w_count):
        board_list[h][w] = temp_list[w]
count = 0
while True:
    if count > 100:
        break
    if board_list[r][c] == k:
        result = count
        break

    if h_count >= w_count:  # 행연산
        max_w = 0
        for h in range(h_count):
            temp_dict = {}
            temp_list = []
            for w in range(w_count):
                if board_list[h][w] == 0:
                    continue
                if board_list[h][w] == -1:
                    break
                if board_list[h][w] not in temp_dict:
                    temp_dict[board_list[h][w]] = 0
                temp_dict[board_list[h][w]] += 1
            for temp_dict_key in temp_dict.keys():
                value = temp_dict[temp_dict_key]
                heapq.heappush(temp_list, (value, temp_dict_key))
            max_w = max(max_w, len(temp_list))
            temp_w = 0
            board_list[h] = [-1] * 200
            while True:
                if len(temp_list) == 0:
                    break
                value, key = heapq.heappop(temp_list)
                board_list[h][temp_w] = key
                board_list[h][temp_w + 1] = value
                temp_w += 2
        w_count = max_w * 2
        for h in range(h_count):
            for w in reversed(range(w_count)):
                if board_list[h][w] != -1:
                    break
                board_list[h][w] = 0
        if w_count > 100:
            for h in range(h_count):
                board_list[h][:100] = board_list[100:]
                board_list[100:] = [-1] * 100



    else:  # 열연산
        max_h = 0
        for w in range(w_count):
            temp_dict = {}
            temp_list = []
            for h in range(h_count):
                if board_list[h][w] == 0:
                    continue
                if board_list[h][w] == -1:
                    break
                if board_list[h][w] not in temp_dict:
                    temp_dict[board_list[h][w]] = 0
                temp_dict[board_list[h][w]] += 1
            for temp_dict_key in temp_dict.keys():
                value = temp_dict[temp_dict_key]
                heapq.heappush(temp_list, (value, temp_dict_key))
            max_h = max(max_h, len(temp_list))
            temp_h = 0
            for i in range(200):
                board_list[i][w] = -1
            while True:
                if len(temp_list) == 0:
                    break
                value, key = heapq.heappop(temp_list)
                board_list[temp_h][w] = key
                board_list[temp_h + 1][w] = value
                temp_h += 2
        h_count = max_h * 2
        for w in (range(w_count)):
            for h in reversed(range(h_count)):
                if board_list[h][w] != -1:
                    break
                board_list[h][w] = 0
        if h_count > 100:
            for w in range(w_count):
                for i in range(100):
                    board_list[i][w] = board_list[100 - i][w]
                for i in range(100, 200):
                    board_list[i][w] = -1
    count += 1
print(result)
