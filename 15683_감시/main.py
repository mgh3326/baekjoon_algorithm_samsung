import sys

sys.stdin = open("data/input.txt")


def dfs(depth):
    global result
    global start_current_value
    if depth == len(cctv_list):
        if result > current_value:
            result = current_value
        return
    current_h, current_w, cctv_idx = cctv_list[depth]
    for cctv_dir_list in cctv_dict[cctv_idx]:
        for cctv_dir in cctv_dir_list:
            # 그리기
            next_h = current_h
            next_w = current_w
            while True:
                next_h += dh[cctv_dir]
                next_w += dw[cctv_dir]
                if next_h >= n or next_w >= m or next_h < 0 or next_w < 0 or board_list[next_h][next_w] == 6:
                    break
                if board_list[next_h][next_w] == 0:
                    board_list[next_h][next_w] = "#"
                    current_value -= 1
                if board_list[next_h][next_w] == 0 or board_list[next_h][next_w] == "#":
                    visit_list[next_h][next_w].append(depth)
        dfs(depth + 1)
        # 지우기
        for cctv_dir in cctv_dir_list:
            next_h = current_h
            next_w = current_w
            while True:
                next_h += dh[cctv_dir]
                next_w += dw[cctv_dir]
                if next_h >= n or next_w >= m or next_h < 0 or next_w < 0 or board_list[next_h][next_w] == 6:
                    break
                if board_list[next_h][next_w] != "#":
                    continue
                visit_list[next_h][next_w].pop()
                if len(visit_list[next_h][next_w]) == 0:
                    board_list[next_h][next_w] = 0
                    current_value += 1


dh = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dw = [0, 1, 0, -1]  # 상, 우, 하, 좌
cctv_dict = {
    1: [[1],  # 우
        [2],
        [3],
        [0]
        ],
    2: [[1, 3],  # 우 좌
        [0, 2]
        ],
    3: [[0, 1],  # 우 상
        [1, 2],
        [2, 3],
        [0, 3],
        ],
    4: [[3, 0, 1],  # 우 #TODO 여기 마지막 행을 누락해서 틀렸었다.
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 0],
        ],
    5: [[0, 1, 2, 3],  # 상 하 좌 우
        ],
}
n, m = map(int, input().split())
board_list = []
visit_list = []
cctv_list = []
result = 0
for h in range(n):
    visit_list.append([])
    temp_list = list(map(int, input().split()))

    for w in range(m):
        visit_list[h].append([])
        if temp_list[w] == 0:
            result += 1
        elif 0 < temp_list[w] < 6:
            cctv_list.append([h, w, temp_list[w]])

    board_list.append(temp_list)
start_current_value = result
dfs(0)
print(result)
