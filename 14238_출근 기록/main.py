import sys

sys.stdin = open("input.txt")


def dfs(depth):
    global current_sum
    global result
    global current_str
    global is_end
    if current_sum > m:  # 백트래킹
        return
    if depth == n:
        if current_sum == m:
            result = current_str
            is_end = True
        return
    for i in range(3):
        temp_sum = 0
        for j in range(i):
            temp_sum += alpha_count_list[j]
        current_sum += temp_sum
        alpha_count_list[i] += 1
        current_str += alpha_list[i]
        dfs(depth + 1)
        if is_end:
            return
        alpha_count_list[i] -= 1
        current_sum -= temp_sum
        current_str = current_str[:-1]


input_str = input()
m = len(input_str)
current_str = ""
result = "-1"
is_end = False
dfs(0)
print(result)
