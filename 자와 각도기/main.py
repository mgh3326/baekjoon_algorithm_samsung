import sys

sys.stdin = open("./data/input.txt")

import itertools

n_len, k_len = map(int, input().split())
n_list = list(map(int, input().split()))
k_list = list(map(int, input().split()))
combinations = list(itertools.combinations(n_list, 2))
my_set = set(n_list)
for combination in combinations:
    hap = combination[0] + combination[1]
    if hap < 360:
        my_set.add(hap)
    cha = abs(combination[0] - combination[1])
    my_set.add(cha)
for k in k_list:
    if k in my_set:
        print("YES")
    else:
        print("NO")
