import sys

sys.stdin = open("./data/input1.txt")


def dfs(depth):
    global result
    if depth == 5:
        return

    for dir_idx in range(len(dir_list)):
        number_list = save_list[-1]
        visit_dict = {}
        current_board_list = [[-1 for _ in range(N)] for _ in range(N)]
        # 회전하기
        dh, dw = dir_list[dir_idx]
        if dir_idx == 0:  # 위쪽 (sort를 w , h순으로)
            number_list.sort(key=lambda x: (x[1], x[0]))
        elif dir_idx == 1:
            number_list.sort(key=lambda x: (x[1], -x[0]))
        elif dir_idx == 2:
            number_list.sort(key=lambda x: (x[0], x[1]))
        elif dir_idx == 3:
            number_list.sort(key=lambda x: (x[0], -x[1]))
        new_number_list = []
        for (current_h, current_w, value) in number_list:
            while True:
                nh, nw = current_h + dh, current_w + dw
                if nh >= N or nw >= N or nh < 0 or nw < 0:
                    current_board_list[current_h][current_w] = len(new_number_list)
                    new_number_list.append([current_h, current_w, value])
                    break
                if current_board_list[nh][nw] != -1:
                    if value == new_number_list[current_board_list[nh][nw]][2] and (nh, nw) not in visit_dict:
                        visit_dict[(nh, nw)] = len(new_number_list)
                        new_number_list[current_board_list[nh][nw]][2] += value
                        result = max(result, new_number_list[current_board_list[nh][nw]][2])
                    else:
                        current_board_list[current_h][current_w] = len(new_number_list)
                        new_number_list.append([current_h, current_w, value])
                    break
                current_h, current_w = nh, nw
        save_list.append(new_number_list)
        dfs(depth + 1)
        save_list.pop()


dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]
result = 0
N = int(input())
first_number_list = []
board_list = [list(map(int, input().split())) for i in range(N)]
for h in range(N):
    for w in range(N):
        if board_list[h][w] != 0:
            first_number_list.append([h, w, board_list[h][w]])
            result = max(result, board_list[h][w])

save_list = []
save_list.append(first_number_list)
dfs(0)
print(result)
