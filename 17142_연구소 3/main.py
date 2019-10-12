import sys

sys.stdin = open("./input.txt")

dir_list = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1],
]


def dfs(current_idx, depth):
    global current_value
    global result
    if depth == m:
        if current_value != 0:
            return
        if result == -1 or result > max(min_space_dict.values()):
            result = max(min_space_dict.values())
        return
    for i in range(virus_len)[current_idx:]:
        start_h, start_w = virus_list[i]
        queue = [[start_h, start_w, 1]]
        visit_set = set()
        visit_set.add((start_h, start_w))
        while True:
            # BFS로 채워가면 되겠다
            if len(queue) == 0:
                break
            current_h, current_w, cost = queue.pop(0)
            for dh, dw in dir_list:
                next_h = dh + current_h
                next_w = dw + current_w
                if next_h < 0 or next_w < 0 or next_h >= n or next_w >= n:
                    continue
                if board_list[next_h][next_w] == 0:
                    if (next_h, next_w) in visit_set:
                        continue
                    visit_set.add((next_h, next_w))
                    queue.append([next_h, next_w, cost + 1])
                    if len(space_dict[(next_h, next_w)]) == 0:
                        current_value -= 1
                    if min_space_dict[(next_h, next_w)] == -1 or min_space_dict[(next_h, next_w)] > cost:
                        min_space_dict[(next_h, next_w)] = cost
                    space_dict[(next_h, next_w)].append(cost)
        dfs(current_idx + 1, depth + 1)
        for current_h, current_w in list(visit_set):
            if current_h == start_h and current_h == start_h:
                continue
            pop = space_dict[(current_h, current_w)].pop()
            if len(space_dict[(current_h, current_w)]) == 0:
                min_space_dict[(current_h, current_w)] = -1
                current_value += 1
            else:
                if pop == min_space_dict[(current_h, current_w)]:
                    min_space_dict[(current_h, current_w)] = min(space_dict[(current_h, current_w)])


n, m = map(int, input().split())
virus_list = []
virus_dict = {}
board_list = []
space_list = []
space_dict = {}
min_space_dict = {}
space_len = 0
virus_len = 0
result = -1
for i in range(n):
    temp_list = list(map(int, input().split()))
    for j in range(n):
        if temp_list[j] == 2:
            virus_list.append([i, j])
            virus_dict[i, j] = 0
            virus_len += 1
        elif temp_list[j] == 0:
            space_list.append([i, j])
            space_dict[i, j] = []
            min_space_dict[i, j] = -1
            space_len += 1

    board_list.append(temp_list)
current_value = space_len

dfs(0, 0)
print(result)
