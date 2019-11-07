import sys

sys.stdin = open("./data/input1.txt")

import math

N = int(input())
A_list = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0
for A in A_list:
    if (A - B) < 0:
        result += 1
    else:
        result += math.ceil((A - B) / C) + 1  # (해결) ceil의 음수조건 유의하자!
print(result)
