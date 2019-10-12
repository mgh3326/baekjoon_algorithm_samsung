import sys

sys.stdin = open("./data/input1.txt", "r")


def inverse_dfs(depth):
    global is_end
    if depth == char_num + 1:
        is_end = True
        return
    for j in reversed(range(10)):
        if j not in my_list:
            if depth > 0:
                if char_list[depth - 1] == '<':
                    if my_list[-1] > j:
                        continue
                else:
                    if my_list[-1] < j:
                        continue
            my_list.append(j)
            inverse_dfs(depth + 1)
            if is_end:
                return
            my_list.pop()


def dfs(depth):
    global is_end
    if depth == char_num + 1:
        is_end = True
        return
    for j in range(10):
        if j not in my_list:
            if depth > 0:
                if char_list[depth - 1] == '<':
                    if my_list[-1] > j:
                        continue
                else:
                    if my_list[-1] < j:
                        continue
            my_list.append(j)
            dfs(depth + 1)
            if is_end:
                return
            my_list.pop()


char_num = int(input())
char_list = input().split()
my_list = []
is_end = False
inverse_dfs(0)
max_result = "".join(map(str, my_list))
my_list.clear()
is_end = False
dfs(0)
min_result = "".join(map(str, my_list))
print(max_result)
print(min_result)
