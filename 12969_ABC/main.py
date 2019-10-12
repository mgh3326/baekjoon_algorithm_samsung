import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())
alpha_list = ["A", "B", "C"]
alpha_dict = {}
memo = []
for i in range(31):
    memo.append(dict())
if 1 not in memo[0]:
    memo[1][0] = set()
memo[1][0].add((1, 0, 0))
memo[1][0].add((0, 1, 0))
memo[1][0].add((0, 0, 1))
# a, b, c (count), value
alpha_dict[((1, 0, 0), 0)] = "A"
alpha_dict[((0, 1, 0), 0)] = "B"
alpha_dict[((0, 0, 1), 0)] = "C"
result = -1
is_end = False
for _index in range(n - 1):
    if is_end:
        break
    index = _index + 1
    for current_value in memo[index].keys():
        if is_end:
            break
        for memo_value in memo[index][current_value]:
            if is_end:
                break
            memo_str = alpha_dict[(memo_value, current_value)]
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
                if index == n - 1 and next_value == m:
                    result = memo_str + alpha_list[i]
                    is_end = True
                    break
                alpha_dict[(tuple(alpha_count_list), next_value)] = memo_str + alpha_list[i]
print(result)
