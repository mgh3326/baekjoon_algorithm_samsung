import sys

sys.stdin = open("./data/input.txt")


# TODO 시간 초과 ( 0% -> 결과값이 3 이상 나오지 않음을 확인 못 함 , 9% -> 결과값 3 초과 -1이 변경)
def dfs(depth, cost):
    if cost > 3:
        return

    def find_combination(_depth, _start_idx):
        if _depth == size:
            # for combination_value in combination:
            #     board_list[depth][combination_value] = True
            dfs(depth + 1, cost + len(combination))
            # for combination_value in combination:
            #     board_list[depth][combination_value] = False
            return
        for _idx in range(_start_idx, len(possible_list)):
            combination.append(possible_list[_idx])
            board_list[depth][possible_list[_idx]] = True
            find_combination(_depth + 1, _idx + 1)
            combination.pop()
            board_list[depth][possible_list[_idx]] = False

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
    depth_ = board_list[depth]
    possible_list = []
    for idx in range(N - 1):
        if idx < N - 1 and depth_[idx]:
            continue
        if idx > 0 and depth_[idx - 1]:
            continue
        if idx < N - 2 and depth_[idx + 1]:
            continue
        possible_list.append(idx)
    for size in range(len(possible_list) + 1):
        if size > 3:
            break
        combination = []
        find_combination(0, 0)


N, M, H = map(int, input().split())

board_list = []
for i in range(H):
    temp_list = [False] * (N - 1)
    board_list.append(temp_list)

for i in range(M):
    a, b = map(int, input().split())
    board_list[a - 1][b - 1] = True
result = -1
dfs(0, 0)
print(result)
