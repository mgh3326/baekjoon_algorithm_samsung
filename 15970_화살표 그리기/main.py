import sys

sys.stdin = open("./data/input.txt")

N = int(input())
color_list = [list() for i in range(N)]
result = 0
for i in range(N):
    x, y = map(int, input().split())
    y -= 1
    color_list[y].append(x)
for y in range(N):
    if len(color_list[y]) <= 1:
        continue
    color_list[y].sort()
    for idx, value in enumerate(color_list[y]):
        left_value = 10 ** 5 + 1
        right_value = 10 ** 5 + 1
        if idx - 1 >= 0:
            left_value = color_list[y][idx] - color_list[y][idx - 1]
        if idx + 1 < len(color_list[y]):
            right_value = color_list[y][idx + 1] - color_list[y][idx]
        result += min(left_value, right_value)
print(result)
