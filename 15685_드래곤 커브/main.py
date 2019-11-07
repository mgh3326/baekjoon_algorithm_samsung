import sys

sys.stdin = open("./data/input.txt")

dir_list = [
    [0, 1],  # 우
    [-1, 0],  # 상
    [0, -1],  # 좌
    [1, 0],  # 하
]
# 우 -> 상 (
# 상 -> 좌
# 좌 -> 하
# 하 -> 우?
N = int(input())
visit_set = set()


def add_visit_set(input_y, input_x):
    if 0 <= input_x <= 100 and 0 <= input_y <= 100:
        visit_set.add((input_y, input_x))


for i in range(N):
    x, y, d, g = map(int, input().split())
    stack = []
    count = 0
    h = y
    w = x
    add_visit_set(h, w)
    dh, dw = dir_list[d]
    h += dh
    w += dw
    add_visit_set(h, w)
    stack.append((d + 1) % len(dir_list))

    while True:
        if count == g:
            break
        stack_len_saved = len(stack)
        for _stack_idx in range(stack_len_saved):
            stack_idx = stack_len_saved - 1 - _stack_idx
            d = stack[stack_idx]
            dh, dw = dir_list[d]
            h += dh
            w += dw
            add_visit_set(h, w)
            stack.append((d + 1) % len(dir_list))

        count += 1
result = 0
for h, w in visit_set:
    if (h + 1, w) in visit_set and (h, w + 1) in visit_set and (h + 1, w + 1) in visit_set:
        result += 1
print(result)