import sys

sys.stdin = open("./data/input.txt")

dir_list = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]
N, M, K = map(int, input().split())
board_list = []
tree_dict = {}

A = []
for n in range(N):
    temp_list = list(map(int, input().split()))
    A.append(temp_list)
    temp_list = [5] * N
    board_list.append(temp_list)
for n in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    if (x, y) not in tree_dict:
        tree_dict[x, y] = []
    tree_dict[x, y].append(z)
result = M

count = 0
while True:
    if count == K:
        break
    # 봄
    temp_dict = {}
    fall_temp_dict = {}

    for h, w in tree_dict.keys():
        current_tree_list = tree_dict[h, w]
        temp_list = []
        for current_tree in current_tree_list:
            if board_list[h][w] >= current_tree:
                board_list[h][w] -= current_tree
                temp_list.append(current_tree + 1)
                if (current_tree + 1) % 5 == 0:
                    for dh, dw in dir_list:
                        nh = h + dh
                        nw = w + dw
                        if nh < 0 or nw < 0 or nh >= N or nw >= N:
                            continue
                        if (nh, nw) not in fall_temp_dict:
                            fall_temp_dict[nh, nw] = 0
                        fall_temp_dict[nh, nw] += 1
            else:
                if (h, w) not in temp_dict:
                    temp_dict[h, w] = 0
                temp_dict[h, w] += current_tree // 2
                result -= 1
        tree_dict[h, w] = temp_list
    # 여름
    for h, w in temp_dict.keys():
        board_list[h][w] += temp_dict[h, w]
    # 가을
    for h, w in fall_temp_dict.keys():
        for _ in range(fall_temp_dict[h, w]):
            if (h, w) not in tree_dict:
                tree_dict[h, w] = []
            tree_dict[h, w].insert(0, 1)
            result += 1

    # 겨울
    for h in range(N):
        for w in range(N):
            board_list[h][w] += A[h][w]
    count += 1

print(result)
