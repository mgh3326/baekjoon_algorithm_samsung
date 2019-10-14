import sys

sys.stdin = open("./input.txt")

import heapq

dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

N = int(input())
board_list = []
start_h = 0
start_w = 0
fish_dict = {}
current_shark_size = 2
fish_count = 0
shark_fish_count = 0
for h in range(N):
    temp_list = list(map(int, input().split()))
    for w in range(N):
        if temp_list[w] == 9:
            start_h = h
            start_w = w
        elif temp_list[w] > 0:
            if temp_list[w] not in fish_dict:
                fish_dict[temp_list[w]] = []
            fish_dict[temp_list[w]].append((h, w))
            fish_count += 1

    board_list.append(temp_list)
result = 0
current_h = start_h
current_w = start_w

while True:
    if fish_count == 0:
        break
    visit_list = []
    for i in range(N):
        temp_list = [-1] * N
        visit_list.append(temp_list)
    visit_list[current_h][current_w] = 0
    current_able_fish_list = []
    for fish_size in fish_dict.keys():
        if fish_size < current_shark_size:
            current_able_fish_list.append(fish_dict[fish_size])
        elif fish_size > current_shark_size:
            for _temp_value in fish_dict[fish_size]:
                visit_list[_temp_value[0]][_temp_value[1]] = -2
    my_list = []
    queue = []
    queue.append([current_h, current_w, 0])
    while True:
        if len(queue) == 0:
            break
        h, w, time = queue.pop(0)
        for dh, dw in dir_list:
            nh = h + dh
            nw = w + dw
            if nh < 0 or nw < 0 or nh >= N or nw >= N or visit_list[nh][nw] != -1:
                continue
            visit_list[nh][nw] = time + 1
            queue.append([nh, nw, time + 1])

    for queue_value in current_able_fish_list:
        for h, w in queue_value:
            if visit_list[h][w] != -1:
                time = visit_list[h][w]
                heapq.heappush(my_list, (time, h, w))
    if len(my_list) == 0:
        break
    time, h, w = heapq.heappop(my_list)
    fish_dict[board_list[h][w]].remove((h, w))
    board_list[h][w] = 0
    current_h = h
    current_w = w
    shark_fish_count += 1
    if shark_fish_count == current_shark_size:
        current_shark_size += 1
        shark_fish_count = 0

    result += time
    fish_count -= 1
print(result)
