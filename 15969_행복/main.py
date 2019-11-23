import sys

sys.stdin = open("./data/input.txt")

N = int(input())
value_list = list(map(int, input().split()))
min_value = 1000
max_value = 0
for value in value_list:
    min_value = min(value, min_value)
    max_value = max(value, max_value)
print(max_value - min_value)
