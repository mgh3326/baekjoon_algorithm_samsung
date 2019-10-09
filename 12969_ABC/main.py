import sys

sys.stdin = open("input.txt")


def dfs(depth):
    global current_sum
    global current_str
    global is_end
    if current_sum > m:  # 백트래킹
        return
    if depth == n:
        if current_sum == m:
            is_end = True
        return
    for i in range(3):
        temp_sum = 0
        if current_alpha_list[i] == 0:
            continue
        for j in range(i):
            temp_sum += temp_alpha_count_list[j]
        current_sum += temp_sum
        if current_sum > m:
            current_sum -= temp_sum
            break
        current_alpha_list[i] -= 1
        temp_alpha_count_list[i] += 1
        current_str += alpha_list[i]
        dfs(depth + 1)
        if is_end:
            return
        temp_alpha_count_list[i] -= 1
        current_alpha_list[i] += 1
        current_sum -= temp_sum
        current_str = current_str[:-1]


n, m = map(int, input().split())
alpha_list = ["A", "B", "C"]
memo = []
for i in range(31):
    memo.append(dict())
if 1 not in memo[0]:
    memo[1][0] = set()
memo[1][0].add((1, 0, 0))
memo[1][0].add((0, 1, 0))
memo[1][0].add((0, 0, 1))
for _index in range(n - 1):
    index = _index + 1
    for current_value in memo[index].keys():
        for memo_value in memo[index][current_value]:
            for i in range(3):
                alpha_count_list = list(memo_value)
                temp_count = 0
                for j in range(i):
                    temp_count += alpha_count_list[j]
                next_value = temp_count + current_value
                if next_value not in memo[index + 1]:
                    memo[index + 1][next_value] = set()
                alpha_count_list[i] += 1
                memo[index + 1][next_value].add(tuple(alpha_count_list))
if m not in memo[n]:
    print("-1")
else:
    current_sum = 0
    current_str = ""
    is_end = False
    temp_alpha_count_list = [0] * 3
    current_alpha_list = list(memo[n][m].pop())
    dfs(0)
    print(current_str)
