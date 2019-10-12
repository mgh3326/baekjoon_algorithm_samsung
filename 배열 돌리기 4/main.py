import sys

sys.stdin = open("./data/input.txt")
# TODO DFS로 다시 짜보도록 하자
import itertools
import copy

# 오른쪽, 아래, 왼쪽 위
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
my_list = [
    [0, 1],
    [1, 1],
    [1, 0],
    [0, 0],
]
n, m, k = map(int, input().split())
origin_board_list = []
for i in range(n):
    temp_list = list(map(int, input().split()))
    origin_board_list.append(temp_list)
rotate_list = []
for i in range(k):
    temp_list = list(map(int, input().split()))
    rotate_list.append(temp_list)
answer = -1
permutations = list(itertools.permutations(rotate_list, len(rotate_list)))
for permutation in permutations:
    board_list = copy.deepcopy(origin_board_list)
    for _permutation in permutation:
        r, c, s = _permutation

        while True:
            start_point = [
                [r - s - 1, c - s - 1],
                [r + s - 1, c + s - 1]
            ]
            current_h, current_w = start_point[0]
            current_value = board_list[current_h][current_w]
            for dir_idx in range(len(dh)):
                while True:
                    next_h = current_h + dh[dir_idx]
                    next_w = current_w + dw[dir_idx]
                    _current_value = board_list[next_h][next_w]
                    board_list[next_h][next_w] = current_value
                    current_value = _current_value
                    current_h, current_w = next_h, next_w
                    if next_h == start_point[my_list[dir_idx][0]][0] and next_w == start_point[my_list[dir_idx][1]][1]:
                        break
            s -= 1
            if s == 0:
                break
    for board in board_list:
        board_sum = sum(board)
        if answer == -1 or answer > board_sum:
            answer = board_sum
print(answer)
