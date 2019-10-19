import sys

sys.stdin = open("./data/input.txt")

import math


def dfs(depth, start_idx):
    global result
    if depth == size:
        number_list_copy = number_list.copy()
        operation_list_copy = operation_list.copy()
        # 괄호 먼저
        for idx in reversed(queue):
            operation = operation_list_copy[idx]
            if operation == "*":
                number_list_copy[idx] *= number_list_copy[idx + 1]
            elif operation == "+":
                number_list_copy[idx] += number_list_copy[idx + 1]
            elif operation == "-":
                number_list_copy[idx] -= number_list_copy[idx + 1]
            number_list_copy.pop(idx + 1)
            operation_list_copy.pop(idx)
        # 나머지 하자
        for idx in (range(len(operation_list_copy))):
            operation = operation_list_copy[idx]
            if operation == "*":
                number_list_copy[1] *= number_list_copy[0]
            elif operation == "+":
                number_list_copy[1] += number_list_copy[0]
            elif operation == "-":
                number_list_copy[1] = number_list_copy[0] - number_list_copy[1]
            number_list_copy.pop(0)
        result = max(result, number_list_copy[0])
        return
    for idx in range(start_idx, len(operation_list)):
        if len(queue) != 0 and idx - queue[-1] == 1:
            continue
        queue.append(idx)
        dfs(depth + 1, idx + 1)
        queue.pop()


n = int(input())
my_str = input()
number_list = []
operation_list = []
result = -2 ** 31
for my_str_index in range(len(my_str)):
    if my_str_index % 2 == 0:
        number_list.append(int(my_str[my_str_index]))
    else:
        operation_list.append(my_str[my_str_index])
for size in range(math.ceil(len(operation_list) / 2) + 1):
    queue = []
    dfs(0, 0)
print(result)
