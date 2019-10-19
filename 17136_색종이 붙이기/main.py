import sys

sys.stdin = open("input.txt")

dirs = [
    [1, 0],
    [0, 1],
]


def dfs(current_idx, depth):
    global result
    global start_current_value
    current_h, current_w = number_list[current_idx % len(number_list)]
    if depth == len(number_list):
        if result == -1 or current_value < result:
            result = current_value
        return
    if result != -1 and current_value >= result:
        return
    if number_dict[(current_h, current_w)]:
        dfs(current_idx + 1, depth + 1)
        return
    temp_list = []
    is_break = False
    for paper_index in range(5):
        h_max = current_h + dirs[0][0] * paper_index
        w_max = current_w + dirs[1][1] * paper_index
        if h_max >= n or w_max >= n:
            break
        if board_list[h_max][w_max] != 1 or number_dict[(h_max, w_max)] is not False:
            break
        temp_list.append([h_max, w_max])
        for _h in range(current_h, h_max):
            if board_list[_h][w_max] != 1 or number_dict[(_h, w_max)] is not False:
                is_break = True
                break
            temp_list.append([_h, w_max])
        for _w in range(current_w, w_max):
            if board_list[h_max][_w] != 1 or number_dict[(h_max, _w)] is not False:
                is_break = True
                break
            temp_list.append([h_max, _w])
        if is_break:
            break
        if paper_list[paper_index] == 0:
            continue
        for _h, _w in temp_list:
            number_dict[(_h, _w)] = True
        paper_list[paper_index] -= 1
        current_value += 1
        dfs(current_idx + 1, depth + 1)
        paper_list[paper_index] += 1
        current_value -= 1
        for _h, _w in temp_list:
            number_dict[(_h, _w)] = False


start_current_value = 0
result = -1
n = 10
board_list = []
number_list = []
number_dict = {}
paper_list = [5] * 5
for h in range(n):
    temp_list = list(map(int, input().split()))
    for w in range(len(temp_list)):
        if temp_list[w] == 1:
            number_list.append([h, w])
            number_dict[(h, w)] = False
    board_list.append(temp_list)
# for number_idx in range(len(first_number_list)):
#     dfs(number_idx, 0)
if len(number_list) == 0:
    result = 0
else:
    dfs(0, 0)
print(result)
