import sys

sys.stdin = open("./data/input.txt")


def dfs(depth):
    global result_max_value
    global result_min_value
    if depth == len(my_list):
        if tuple(queue) in save_set:  # 이미 했어
            return
        save_set.add(tuple(queue))
        current_value = number_list[0]
        for my_idx in range(len(my_list)):
            if queue[my_idx] == 0:
                current_value += number_list[my_idx + 1]
            elif queue[my_idx] == 1:
                current_value -= number_list[my_idx + 1]
            elif queue[my_idx] == 2:
                current_value *= number_list[my_idx + 1]
            elif queue[my_idx] == 3:
                if current_value < 0:
                    current_value *= -1
                    current_value //= number_list[my_idx + 1]
                    current_value *= -1
                else:
                    current_value //= number_list[my_idx + 1]
        if result_max_value < current_value:
            result_max_value = current_value
        if result_min_value > current_value:
            result_min_value = current_value
        return
    for idx in range(len(my_list)):
        if visit_list[idx]:
            continue
        visit_list[idx] = True
        queue.append(my_list[idx])
        dfs(depth + 1)
        visit_list[idx] = False
        queue.pop()


N = int(input())
result_max_value = -1000000000
result_min_value = 1000000000
number_list = list(map(int, input().split()))
value_list = list(map(int, input().split()))
my_list = []
for i in range(len(value_list)):
    my_list.extend([i] * value_list[i])

save_set = set()
visit_list = [False] * len(my_list)
queue = []
dfs(0)
print(result_max_value)
print(result_min_value)
