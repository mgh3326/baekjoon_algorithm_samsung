import sys

sys.stdin = open("./data/input.txt")

sys.setrecursionlimit(10 ** 6)


def dfs(depth):
    global result
    global is_finish
    if depth == end_idx:
        is_finish = True
        # temp_max = 0
        # temp_sum = 0
        # for temp_idx in range(len(temp_list) - 1):
        #     temp = board_list[temp_list[temp_idx]][temp_list[temp_idx + 1]]
        #     temp_max = max(temp, temp_max)
        #     temp_sum += temp
        # temp_sum -= temp_max
        # result = temp_sum
        result -= max(oh_list)
        return
    for value in board_list[depth].keys():
        if value in visit_set:
            continue
        visit_set.add(value)
        if len(temp_list) > 0:
            result += board_list[temp_list[-1]][value]
            oh_list.append(board_list[temp_list[-1]][value])

        temp_list.append(value)
        dfs(value)
        if is_finish:
            return
        if len(temp_list) > 1:
            result -= board_list[temp_list[-2]][temp_list[-1]]
            oh_list.pop()
        temp_list.pop()
        visit_set.remove(value)


is_finish = False
N, start_idx, end_idx = map(int, input().split())
start_idx -= 1
end_idx -= 1
board_list = [dict() for i in range(N)]
for i in range(N - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    board_list[a][b] = c
    board_list[b][a] = c
visit_set = set()
visit_set.add(start_idx)
temp_list = [start_idx]
result = 0
oh_list = []
dfs(start_idx)
print(result)
