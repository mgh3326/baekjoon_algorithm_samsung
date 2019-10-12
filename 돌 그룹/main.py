import sys

sys.stdin = open("./data/input.txt")

import itertools

stone_list = list(map(int, input().split()))
visit_set = set()
stone_list.sort()
visit_set.add(tuple(stone_list))
queue = []
queue.append(stone_list)
result = 0
while True:
    if len(queue) == 0 or result == 1:
        break
    stone_list = queue.pop(0)
    if stone_list[0] == stone_list[1] == stone_list[2]:
        result = 1
        break
    for g1, g2, rest_g in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:

        if stone_list[g1] != stone_list[g2]:
            stone_max = max(stone_list[g1], stone_list[g2])
            stone_min = min(stone_list[g1], stone_list[g2])
            temp_list = [stone_list[rest_g], stone_max - stone_min, stone_min + stone_min]
            temp_list.sort()
            if tuple(temp_list) not in visit_set:
                if temp_list[0] == temp_list[1] == temp_list[2]:
                    result = 1
                    break
                visit_set.add(tuple(temp_list))
                queue.append(temp_list)

# 0,1
# 0,2
# 1,2
print(result)
