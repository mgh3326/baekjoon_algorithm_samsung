# 기존 코드 (속도가 두배가량 느리다) -> 최소값을 찾는거라면 최소값을 먼저 넣어서 백트래킹을 이루는 것이 이상적인 결과를 가져올수 있다.
def dfs(depth, cost):
    if cost > 3:
        return
    global result
    if result != -1 and result <= cost:
        return
    if depth == H:
        for start_idx in range(N):
            current_idx = start_idx
            for h in range(H):
                if current_idx < N - 1 and board_list[h][current_idx]:
                    current_idx += 1
                elif current_idx > 0 and board_list[h][current_idx - 1]:
                    current_idx -= 1
            if start_idx != current_idx:
                break
            if start_idx == N - 1:
                if result == -1 or result > cost:
                    result = cost
        return
    for current_combination in combination_list[depth]:
        if result != -1 and result <= cost:
            return
        if cost + len(current_combination) > 3:
            return
        for value in current_combination:
            board_list[depth][value] = True
        dfs(depth + 1, cost + len(current_combination))
        for value in current_combination:
            board_list[depth][value] = False


def find_combination(_depth, _start_idx):
    if _depth == size:
        temp_combination_list.append(combination.copy())
        return
    for _idx in range(_start_idx, len(possible_list[com_h])):
        if len(combination) != 0 and combination[-1] == possible_list[com_h][_idx] - 1:
            continue
        combination.append(possible_list[com_h][_idx])
        find_combination(_depth + 1, _idx + 1)
        combination.pop()


N, M, H = map(int, input().split())
board_list = []

possible_list = []

for i in range(H):
    temp_list = [False] * (N - 1)
    board_list.append(temp_list)

for i in range(M):
    a, b = map(int, input().split())
    board_list[a - 1][b - 1] = True
for i in range(H):
    temp_possible_list = []
    for idx in range(N - 1):
        if idx < N - 1 and board_list[i][idx]:
            continue
        if idx > 0 and board_list[i][idx - 1]:
            continue
        if idx < N - 2 and board_list[i][idx + 1]:
            continue
        temp_possible_list.append(idx)
    possible_list.append(temp_possible_list)
result = -1
# 가능한 조합을 미리 만들자
combination_list = []
for com_h in range(H):
    temp_combination_list = []
    for size in range(len(possible_list[com_h]) + 1):
        combination = []
        if size > 3:
            break
        find_combination(0, 0)
    combination_list.append(temp_combination_list)
dfs(0, 0)
print(result)
