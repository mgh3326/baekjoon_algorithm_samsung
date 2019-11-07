import sys

sys.stdin = open("./data/input.txt")


def dfs(depth, input_value=-1):
    global result
    if depth == current_length:
        difference_set = total_set.difference(current_set)
        # current_set과 difference_set이 신장트리 임을 확인하고, 된다면 result값을 바꾸도록 하자

        for _set in [current_set, difference_set]:

            temp_set = set()
            pop = _set.pop()
            _set.add(pop)
            queue = [pop]
            temp_set.add(pop)
            while True:
                if len(queue) == 0:
                    break
                pop = queue.pop()
                for value in board_list[pop]:
                    if value in _set and value not in temp_set:
                        temp_set.add(value)
                        queue.append(value)
            if temp_set != _set:
                break
        else:
            current_value = 0
            for current_set_value in current_set:
                current_value += value_list[current_set_value]
            for difference_set_value in difference_set:
                current_value -= value_list[difference_set_value]
            if result == -1 or result > abs(current_value):
                result = abs(current_value)

        return
    for i in range(input_value + 1, n):
        if i in current_set:
            continue
        current_set.add(i)
        dfs(depth + 1, i)
        current_set.remove(i)


n = int(input())
value_list = list(map(int, input().split()))
board_list = []
result = -1
temp_list = []
for i in range(n):
    temp_list.append(i)
total_set = set(temp_list)
visit_list = [False] * n
for _ in range(n):
    temp_list = list(map(int, input().split()))
    temp_list = temp_list[1:]
    oh_list = []
    for temp in temp_list:
        oh_list.append(temp - 1)
    board_list.append(oh_list)
for current_length in range(n // 2):
    current_length += 1
    current_set = set()
    dfs(0)
print(result)
