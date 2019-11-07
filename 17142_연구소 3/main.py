import sys

sys.stdin = open("./input.txt")

dir_list = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1],
]


def dfs(current_idx, depth):
    global start_current_value
    global result
    if depth == m:
        temp_set = set()
        queue = []
        temp_count = 0
        max_cost = 0
        for virus_idx in virus_set:
            queue.append([virus_list[virus_idx], 0, False])
            temp_set.add(tuple(virus_list[virus_idx]))
        while True:
            if len(queue) == 0:
                break
            [current_h, current_w], cost, is_blank = queue.pop(0)
            if result != -1 and cost > result:
                return  # 백트래킹
            if is_blank and cost > max_cost:
                max_cost = cost
            for dir_h, dir_w in dir_list:
                nh = current_h + dir_h
                nw = current_w + dir_w
                if (nh >= n or nw >= n or nh < 0 or nw < 0) or (nh, nw) in temp_set:
                    continue
                if board_list[nh][nw] == 0:
                    temp_set.add((nh, nw))
                    queue.append([[nh, nw], cost + 1, True])
                    temp_count += 1
                if board_list[nh][nw] == 2:
                    temp_set.add((nh, nw))
                    queue.append([[nh, nw], cost + 1, False])
        if temp_count == space_len:
            if result == -1 or result > max_cost:
                result = max_cost
        return

    for i in range(virus_len)[current_idx:]:
        if i + 1 in virus_set:
            continue
        virus_set.add(i)
        dfs(i + 1, depth + 1)
        virus_set.remove(i)


n, m = map(int, input().split())
virus_list = []
board_list = []
space_len = 0
virus_len = 0
result = -1
for i in range(n):
    temp_list = list(map(int, input().split()))
    for j in range(n):
        if temp_list[j] == 2:
            virus_list.append([i, j])
            virus_len += 1
        elif temp_list[j] == 0:
            space_len += 1

    board_list.append(temp_list)
start_current_value = space_len
my_list = []
virus_set = set()
dfs(0, 0)
print(result)
