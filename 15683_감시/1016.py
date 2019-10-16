import sys

sys.stdin = open("./data/input.txt")

dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]
cctv_dict = {
    # 상 하 좌 우
    1: [[0], [1], [2], [3]],
    # 상하, 좌우
    2: [[0, 1], [2, 3]],
    # 상우, 우하, 하좌, 좌상
    3: [[0, 3], [3, 1], [1, 2], [2, 0]],
    # 좌상우, 상우하, 우하좌, 하좌상
    4: [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
    5: [[0, 1, 2, 3]],
}


def dfs(depth):
    global blank_count
    global result
    if result == 0:
        return
    if depth == len(cctv_list):
        if result > blank_count:
            result = blank_count
        return
    h, w = cctv_list[depth]
    for cctv_dirs in cctv_dict[board_list[h][w]]:
        for cctv_dir in cctv_dirs:  # 그리기
            nh, nw = h, w
            while True:
                dh, dw = dir_list[cctv_dir]
                nh, nw = dh + nh, dw + nw
                if nh < 0 or nw < 0 or nh >= N or nw >= M or board_list[nh][nw] == 6:  # 마지막 혹은 벽 발견
                    break
                if visit_list[nh][nw] >= 0:
                    if visit_list[nh][nw] == 0:
                        blank_count -= 1
                    visit_list[nh][nw] += 1

        dfs(depth + 1)
        for cctv_dir in cctv_dirs:  # 지우기
            nh, nw = h, w
            while True:
                dh, dw = dir_list[cctv_dir]
                nh, nw = dh + nh, dw + nw
                if nh < 0 or nw < 0 or nh >= N or nw >= M or board_list[nh][nw] == 6:  # 마지막 혹은 벽 발견
                    break
                if visit_list[nh][nw] >= 0:
                    visit_list[nh][nw] -= 1
                    if visit_list[nh][nw] == 0:
                        blank_count += 1


N, M = map(int, input().split())

board_list = []
cctv_list = []
visit_list = []
blank_count = 0

for _h in range(N):
    temp_list = list(map(int, input().split()))
    cctv_temp_list = [0] * M
    for _w in range(M):
        if 1 <= temp_list[_w] <= 5:
            cctv_list.append((_h, _w))
            cctv_temp_list[_w] = -1
        elif temp_list[_w] == 0:
            blank_count += 1
        else:
            cctv_temp_list[_w] = -1
    board_list.append(temp_list)
    visit_list.append(cctv_temp_list)
result = blank_count

dfs(0)
print(result)
