import sys

sys.stdin = open("data/input.txt")

dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]


def dfs(depth, start_idx):
    global start_current_value
    global result
    if depth == 3:
        current_value = start_current_value
        queue = []
        visit_list = [[-1 for _ in range(M)] for _ in range(N)]
        for virus in virus_list:
            queue.append([virus, 0])
            visit_list[virus[0]][virus[1]] = 0
        queue_idx = 0
        while True:
            if queue_idx >= len(queue):
                break
            (ch, cw), cost = queue[queue_idx]
            for dh, dw in dir_list:
                nh, nw = ch + dh, cw + dw
                if nh < 0 or nw < 0 or nh >= N or nw >= M or board_list[nh][nw] != 0 or (visit_list[nh][nw] != -1):
                    continue
                visit_list[nh][nw] = cost + 1
                queue.append([(nh, nw), cost + 1])
                current_value -= 1
                if current_value <= result:
                    return
            queue_idx += 1
        if current_value > result:
            result = current_value
        return
    for idx in range(start_idx, len(empty_list)):
        h, w = empty_list[idx]
        board_list[h][w] = 1
        dfs(depth + 1, idx + 1)
        board_list[h][w] = 0


N, M = map(int, input().split())
board_list = [list(map(int, input().split())) for i in range(N)]
empty_list = []
virus_list = []
for h in range(N):
    for w in range(M):
        if board_list[h][w] == 0:
            empty_list.append((h, w))
        elif board_list[h][w] == 2:
            virus_list.append((h, w))
start_current_value = len(empty_list) - 3
result = 0
dfs(0, 0)
print(result)
