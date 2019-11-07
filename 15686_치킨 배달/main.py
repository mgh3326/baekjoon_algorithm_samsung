import sys

sys.stdin = open("./data/input.txt")


def dfs(depth, idx):
    if depth == M:
        global result
        _temp_value = 0
        for current_home_idx in range(len(home_list)):
            temp_min = -1
            for save in save_list:
                if temp_min == -1 or temp_min > visit_list[current_home_idx][save]:
                    temp_min = visit_list[current_home_idx][save]
            _temp_value += temp_min
        if result == -1 or result > _temp_value:
            result = _temp_value
        return
    for i in range(idx, len(chicken_list)):
        save_list.append(i)
        dfs(depth + 1, i + 1)
        save_list.pop()


N, M = map(int, input().split())
result = -1
board_list = []
home_list = []
chicken_list = []
for h in range(N):
    temp_list = list(map(int, input().split()))
    for w in range(N):
        if temp_list[w] == 1:
            home_list.append((h, w))
        elif temp_list[w] == 2:
            chicken_list.append((h, w))
    board_list.append(temp_list)
visit_list = []
for home_idx in range(len(home_list)):
    temp_list = []
    for chicken_idx in range(len(chicken_list)):
        temp_value = abs(chicken_list[chicken_idx][0] - home_list[home_idx][0]) + abs(
            chicken_list[chicken_idx][1] - home_list[home_idx][1])

        temp_list.append(temp_value)
    visit_list.append(temp_list)
save_list = []
dfs(0, 0)
print(result)
