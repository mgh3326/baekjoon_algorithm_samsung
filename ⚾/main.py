import sys

sys.stdin = open("./data/input.txt")

import itertools

N = int(input())
board_list = []
for i in range(N):
    temp_list = list(map(int, input().split()))
    board_list.append(temp_list)

result = 0
# 5,6,7,8,9 이닝 애들 순서를 바꿔 본 것중에 최고 값을 찾아보자
gojung = 0
find_list = [1, 2, 3, 4, 5, 6, 7, 8]
permutations = list(itertools.permutations(find_list, len(find_list)))
for permutation in permutations:
    position_list = list(permutation)
    position_list.insert(3, gojung)
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
                base_3 = base_2
                base_2 = base_1
                base_1 = True
            elif board_list[current_inning][position_list[current_index]] == 2:
                current_result += (base_3 + base_2)
                base_3 = base_1
                base_2 = True
                base_1 = False
            elif board_list[current_inning][position_list[current_index]] == 3:
                current_result += (base_3 + base_2 + base_1)
                base_3 = True
                base_2 = False
                base_1 = False
            elif board_list[current_inning][position_list[current_index]] == 4:
                current_result += (base_3 + base_2 + base_1 + 1)
                base_3 = False
                base_2 = False
                base_1 = False
            current_index = (current_index + 1) % 9
    if result < current_result:
        result = current_result
print(result)
