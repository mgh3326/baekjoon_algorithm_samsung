import sys

sys.stdin = open("./data/input.txt")


def dfs(depth, start_idx):
    global result
    if depth == N // 2:
        if tuple(queue_set) in save_set:
            return
        difference = total_set.difference(queue_set)
        save_set.add(tuple(queue_set))
        save_set.add(tuple(difference))
        current_value = 0
        for i in queue_set:
            for j in queue_set:
                if i == j:
                    continue
                current_value += (board_list[i][j])
        for i in difference:
            for j in difference:
                if i == j:
                    continue
                current_value -= (board_list[i][j])
        abs_value = abs(current_value)
        if result == -1 or result > abs_value:
            result = abs_value
        return
    for idx in range(start_idx, N):
        queue_set.add(idx)
        dfs(depth + 1, idx + 1)
        queue_set.remove(idx)


N = int(input())
board_list = []
for i in range(N):
    board_list.append(list(map(int, input().split())))
result = -1
total_set = set(i for i in range(N))
save_set = set()
queue_set = set()

dfs(0, 0)
print(result)
