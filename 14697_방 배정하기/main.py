import sys

sys.stdin = open("./data/input.txt")


def dfs(depth):
    global value
    global result
    if depth == 3:
        if value == 0:
            result = 1
        return
    count = 0
    while True:
        if value_list[depth] * count > value:
            break
        value -= value_list[depth] * count
        dfs(depth + 1)
        if result == 1:
            return
        value += value_list[depth] * count
        count += 1


n1, n2, n3, value = map(int, input().split())
value_list = [n1, n2, n3]
result = 0
dfs(0)
print(result)
