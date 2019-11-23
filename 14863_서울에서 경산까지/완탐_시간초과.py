import sys

sys.stdin = open("./data/input.txt")


def dfs(depth):
    global current_time
    global current_cost
    global result
    if current_time > K:  # 백 트래킹
        return
    if depth == N:
        result = max(current_cost, result)
        return
    # 자전거
    current_time += board_list[depth][2]
    current_cost += board_list[depth][3]
    dfs(depth + 1)
    current_time -= board_list[depth][2]
    current_cost -= board_list[depth][3]
    # 도보
    current_time += board_list[depth][0]
    current_cost += board_list[depth][1]
    dfs(depth + 1)
    current_time -= board_list[depth][0]
    current_cost -= board_list[depth][1]


N, K = map(int, input().split())
board_list = [list(map(int, input().split())) for _ in range(N)]
current_time = 0
current_cost = 0
result = 0
dfs(0)
print(result)
