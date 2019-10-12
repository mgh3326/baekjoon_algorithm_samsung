import sys

sys.stdin = open("./data/input.txt")

from collections import deque

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

R, C = list(map(int, sys.stdin.readline().split()))
base_map = [[] for _ in range(R)]
for r in range(R):
    base_map[R - r - 1] = list(sys.stdin.readline().replace('\n', ''))
N = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))

move_dir = 1  # 1이 오른쪽으로 가는거, -1 이 왼쪽으로 가는거
for h_i, height in enumerate(heights):
    # print('\n', h_i, height, move_dir)
    c = 0 if move_dir == 1 else C - 1
    no_mineral = False
    while base_map[height - 1][c] != 'x':

        c += move_dir
        if c >= C or c < 0:
            no_mineral = True
            break
        # print(height-1, c)
    # 해당 층에 미네랄이 없을때
    if no_mineral:
        continue

    # base_map[height-1][c] 이 'x' 일때
    base_map[height - 1][c] = '.'
    visited = []

    for dir in dirs:
        cluster_list = []
        stack = deque()
        dr, dc = dir
        sr, sc = height - 1, c
        nr, nc = sr + dr, sc + dc
        if nr <= 0 or nr >= R or nc < 0 or nc >= C:  # 경계 확인
            continue
        if base_map[nr][nc] == 'x':
            if not (nr, nc) in visited:
                stack.append((nr, nc))
                cluster_list.append((nr, nc))
                visited.append((nr, nc))

        while stack:
            sr, sc = stack.pop()
            for dir in dirs:  # 해당 좌표 사방에 클러스터가 있는지 확인
                dr, dc = dir
                nr, nc = sr + dr, sc + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C:  # 경계 확인
                    continue
                if base_map[nr][nc] != 'x':
                    continue
                if nr == 0:  # 밑에 까지 이어지기 때문에
                    stack.clear()
                    cluster_list.clear()
                    break
                else:  # 클러스트에 포함되는지 더 확인해야해
                    if not (nr, nc) in cluster_list:
                        cluster_list.append((nr, nc))
                        stack.append((nr, nc))
                        visited.append((nr, nc))

        if cluster_list:  # 공중에 떠 있는 클러스트가 있을 때
            for cluster in cluster_list:
                cr, cc = cluster
                base_map[cr][cc] = '.'
            move_height, suc_move_height = -2, -1

            move_is_ok = True
            while move_is_ok:
                for cluster in cluster_list:
                    cr, cc = cluster
                    if cr + move_height >= 0:  # 내려갈 길이 있는지 확인
                        if base_map[cr + move_height][cc] != '.':
                            move_is_ok = False
                            break
                    else:
                        move_is_ok = False
                        break

                if move_is_ok:
                    suc_move_height = move_height
                    move_height += -1

            for cluster in cluster_list:
                cr, cc = cluster
                base_map[cr + suc_move_height][cc] = 'x'
            break

    # for i, r in enumerate(reversed(base_map)):
    #   print(R - i, end=" ")
    #   print(*r)

    move_dir *= -1  # 반대쪽에서 다시 시작

for r in reversed(range(R)):
    for c in range(C):
        print(base_map[r][c], end="")
    print("")
