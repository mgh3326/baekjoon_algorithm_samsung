import sys

sys.stdin = open("./data/input.txt")

dir_list = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
]  # →, ←, ↑, ↓
N, K = map(int, input().split())
board_list = [list(map(int, input().split())) for i in range(N)]
mal_list = []
result = -1
for i in range(K):
    r, c, dir_idx = map(int, input().split())
    mal_list.append([r - 1, c - 1, dir_idx - 1])
count = 1
save_list = [[list() for _ in range(N)] for _ in range(N)]
for idx, (h, w, dir_idx) in enumerate(mal_list):
    save_list[h][w].append(idx)
while True:
    if result != -1 or count > 1000:
        break

    for idx, (h, w, dir_idx) in enumerate(mal_list):
        dh, dw = dir_list[dir_idx]
        nh, nw = h + dh, w + dw
        if nh >= N or nw >= N or nh < 0 or nw < 0 or board_list[nh][nw] == 2:  # 파란색
            if mal_list[idx][2] % 2 == 0:
                mal_list[idx][2] += 1
            else:
                mal_list[idx][2] -= 1
            dh, dw = dir_list[mal_list[idx][2]]
            nh, nw = h + dh, w + dw
            if nh >= N or nw >= N or nh < 0 or nw < 0 or board_list[nh][nw] == 2:  # 파란색
                pass
            else:
                if board_list[nh][nw] == 0:  # 흰색
                    for temp_idx in save_list[h][w][save_list[h][w].index(idx):]:
                        mal_list[temp_idx][0] = nh
                        mal_list[temp_idx][1] = nw
                    save_list[nh][nw].extend(save_list[h][w][save_list[h][w].index(idx):])
                    save_list[h][w] = save_list[h][w][:save_list[h][w].index(idx)]
                    if len(save_list[nh][nw]) >= 4:
                        result = count
                elif board_list[nh][nw] == 1:  # 빨간색
                    for temp_idx in save_list[h][w][save_list[h][w].index(idx):]:
                        mal_list[temp_idx][0] = nh
                        mal_list[temp_idx][1] = nw
                    save_list[nh][nw].extend(reversed(save_list[h][w][save_list[h][w].index(idx):]))
                    save_list[h][w] = save_list[h][w][:save_list[h][w].index(idx)]
                    if len(save_list[nh][nw]) >= 4:
                        result = count
        elif board_list[nh][nw] == 0:  # 흰색
            for temp_idx in save_list[h][w][save_list[h][w].index(idx):]:
                mal_list[temp_idx][0] = nh
                mal_list[temp_idx][1] = nw
            save_list[nh][nw].extend(save_list[h][w][save_list[h][w].index(idx):])
            save_list[h][w] = save_list[h][w][:save_list[h][w].index(idx)]
            if len(save_list[nh][nw]) >= 4:
                result = count
        elif board_list[nh][nw] == 1:  # 빨간색
            for temp_idx in save_list[h][w][save_list[h][w].index(idx):]:
                mal_list[temp_idx][0] = nh
                mal_list[temp_idx][1] = nw
            save_list[nh][nw].extend(reversed(save_list[h][w][save_list[h][w].index(idx):]))
            save_list[h][w] = save_list[h][w][:save_list[h][w].index(idx)]
            if len(save_list[nh][nw]) >= 4:
                result = count
    count += 1
print(result)
