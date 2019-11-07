import sys

sys.stdin = open("./data/input.txt")

import sys
import itertools

N = int(sys.stdin.readline())
board_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0
# 5,6,7,8,9 이닝 애들 순서를 바꿔 본 것중에 최고 값을 찾아보자
for permutation in itertools.permutations(range(1, 9), 8):
    position_list = list(permutation[:3]) + [0] + list(permutation[3:])
    current_index = 0
    current_result = 0
    for current_inning in range(N):
        base_1, base_2, base_3 = False, False, False
        out_count = 0
        while True:  # Game Start
            if out_count == 3:
                break
            if board_list[current_inning][position_list[current_index]] == 0:
                out_count += 1
            elif board_list[current_inning][position_list[current_index]] == 1:
                current_result += base_3
                base_3, base_2, base_1 = base_2, base_1, True
            elif board_list[current_inning][position_list[current_index]] == 2:
                current_result += (base_3 + base_2)
                base_3, base_2, base_1 = base_1, True, False
            elif board_list[current_inning][position_list[current_index]] == 3:
                current_result += (base_3 + base_2 + base_1)
                base_3, base_2, base_1 = True, False, False
            elif board_list[current_inning][position_list[current_index]] == 4:
                current_result += (base_3 + base_2 + base_1 + 1)
                base_3, base_2, base_1 = False, False, False
            current_index = (current_index + 1) % 9
    result = max(result, current_result)
print(result)
