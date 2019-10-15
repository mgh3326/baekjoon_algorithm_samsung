import sys

sys.stdin = open("./data/input.txt")

from collections import deque

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
tree_set = set()
tree_list = deque()
A = []
for n in range(N):
    temp_list = list(map(int, input().split()))
    A.append(temp_list)
    temp_list = [5] * N
    board_list.append(temp_list)
    temp_list = []
    for _ in range(N):
        temp_list.append(list() * N)
    tree_list.append(temp_list)

for n in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    if (x, y) not in tree_set:
        tree_set.add((x, y))
    tree_list[x][y].append(z)
result = M

count = 0
while True:
    if count == K:
        break
    # 봄
    temp_dict = {}
    fall_temp_dict = {}
    remove_set_list = []
    for h, w in tree_set:
        current_tree_list = tree_list[h][w]
        for current_tree_idx in range(len(current_tree_list)):
            current_tree = current_tree_list[len(current_tree_list) - current_tree_idx - 1]
            if board_list[h][w] >= current_tree:
                board_list[h][w] -= current_tree
                current_tree_list[len(current_tree_list) - current_tree_idx - 1] = (current_tree + 1)
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
                dead_list = current_tree_list[:len(current_tree_list) - current_tree_idx - 1 + 1]
                if current_tree_idx == 0:
                    remove_set_list.append((h, w))
                tree_list[h][w] = current_tree_list[len(current_tree_list) - current_tree_idx - 1 + 1:]
                for dead in dead_list:
                    board_list[h][w] += dead // 2
                    result -= 1
                break
    for remove_set in remove_set_list:
        tree_set.remove(remove_set)

    # 여름
    # for h, w in temp_dict.keys():
    #     board_list[h][w] += temp_dict[h, w]
    # 가을
    for h, w in fall_temp_dict.keys():
        if (h, w) not in tree_set:
            tree_set.add((h, w))
        tree_list[h][w].extend([1] * fall_temp_dict[h, w])
        result += fall_temp_dict[h, w]

    # 겨울
    for h in range(N):
        for w in range(N):
            board_list[h][w] += A[h][w]
    count += 1

print(result)
