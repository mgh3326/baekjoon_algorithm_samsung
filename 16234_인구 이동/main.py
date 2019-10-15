import sys

sys.stdin = open("./data/input.txt")

import copy
dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

N, L, R = map(int, input().split())
board_list = []
total_visit_list = []
first_open_list = []
for i in range(N):
    temp_list = list(map(int, input().split()))
    board_list.append(temp_list)
    temp_list = [False] * N
    total_visit_list.append(temp_list)
    temp_list = []
    for _ in range(N):
        temp_list.append([])
    first_open_list.append(temp_list)
result = 0
while True:
    visit_list = copy.deepcopy(total_visit_list)
    open_list = copy.deepcopy(first_open_list)
    for h in range(N):
        for w in range(N):
            for dh, dw in dir_list:
                nh = h + dh
                nw = w + dw
                if nh < 0 or nw < 0 or nh >= N or nw >= N or (nh, nw) in open_list[h][w]:
                    continue
                if L <= abs(board_list[h][w] - board_list[nh][nw]) <= R:
                    open_list[h][w].append((nh, nw))
                    open_list[nh][nw].append((h, w))
    is_ok = False
    for h in range(N):
        for w in range(N):
            if visit_list[h][w]:
                continue
            queue = [(h, w)]
            visit_list[h][w] = True
            queue_idx = 0
            temp_sum = board_list[h][w]
            while True:
                if queue_idx >= len(queue):
                    for nh, nw in queue:
                        board_list[nh][nw] = temp_sum // len(queue)
                    break
                current_h, current_w = queue[queue_idx]
                queue_idx += 1
                for nh, nw in open_list[current_h][current_w]:
                    if visit_list[nh][nw]:
                        continue
                    visit_list[nh][nw] = True
                    temp_sum += board_list[nh][nw]
                    is_ok = True
                    queue.append((nh, nw))
    if not is_ok:
        break
    result += 1

print(result)
