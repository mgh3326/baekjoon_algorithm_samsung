import sys

sys.stdin = open("./data/input.txt")

import itertools
import copy

N, M, D = map(int, input().split())
first_enemy_dict = {i: [] for i in range(M)}
first_enemy_count = 0
result = 0
for i in range(N):
    temp_list = list(map(int, input().split()))
    for w in range(len(temp_list)):
        if temp_list[w] == 1:
            first_enemy_dict[w].append(N - i)
            first_enemy_count += 1

for archer_w_list in itertools.combinations(range(M), 3):
    enemy_dict = copy.deepcopy(first_enemy_dict)
    enemy_count = first_enemy_count
    hunting_count = 0
    current_distance = D
    current_level = 1
    while True:
        if current_level > N + 1:
            break
        remove_w_set = set()
        for archer_w in archer_w_list:
            min_value = -1
            min_w_idx = -1
            for enemy_w in enemy_dict.keys():
                if len(enemy_dict[enemy_w]) == 0:
                    continue
                if abs(enemy_w - archer_w) + enemy_dict[enemy_w][-1] <= current_distance + current_level - 1:
                    if min_value == -1 or abs(enemy_w - archer_w) + enemy_dict[enemy_w][-1] < min_value:
                        min_value = abs(enemy_w - archer_w) + enemy_dict[enemy_w][-1]
                        min_w_idx = enemy_w
            if min_w_idx != -1:
                if min_w_idx not in remove_w_set:
                    hunting_count += 1
                    remove_w_set.add(min_w_idx)

        for remove_w in remove_w_set:
            enemy_dict[remove_w].pop()
            if len(enemy_dict[remove_w]) == 0:
                enemy_dict.pop(remove_w)
        for enemy_w in list(enemy_dict.keys()):
            for idx in reversed(range(len(enemy_dict[enemy_w]))):
                if enemy_dict[enemy_w][idx] <= current_level:
                    enemy_dict[enemy_w].pop()
                else:
                    break
            if len(enemy_dict[enemy_w]) == 0:
                enemy_dict.pop(enemy_w)
        current_level += 1
    result = max(result, hunting_count)
print(result)
