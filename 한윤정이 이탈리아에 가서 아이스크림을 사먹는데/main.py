import sys

sys.stdin = open("./data/input.txt")

import itertools

n_len, m_len = map(int, input().split())
m_list = []
for i in range(m_len):
    temp_list = set(map(int, input().split()))
    m_list.append(temp_list)
temp_list = []
for i in range(n_len):
    temp_list.append(i+1)

combinations = list(itertools.combinations(temp_list, 3))
result = 0
for combination in combinations:
    s = set(combination)
    is_correct = True
    for m in m_list:
        if len(s.intersection(m)) == len(m):
            is_correct = False
            break
    if is_correct:
        result += 1
print(result)
