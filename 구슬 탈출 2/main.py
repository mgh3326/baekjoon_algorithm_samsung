import sys
import copy

sys.stdin = open("./data/input1.txt", "r")
# a = open("./data/output1.txt", "r").read()
# print(a)

dh = [-1, 0, 1, 0]  # 상 좌 하 우
dw = [0, -1, 0, 1]  # 상 자 하 우


def dfs(input_depth, input_dir_idx):
    global result
    is_end = False

    if input_depth >= depth_max or (result != -1 and input_depth > result):
        return
    if input_depth != -1:
        blue_point = point_list[0]
        red_point = point_list[1]
        nh, nw = dh[input_dir_idx], dw[input_dir_idx]
        next_blue_point = blue_point[0] + nh, blue_point[1] + nw
        next_red_point = red_point[0] + nh, red_point[1] + nw
        next_blue_value = my_list[next_blue_point[0]][next_blue_point[1]]
        next_red_value = my_list[next_red_point[0]][next_red_point[1]]
        if next_blue_value == next_red_value == 1:  # 벽에 막혔을 경우
            return
        if next_blue_value == 0:
        elif next_blue_value == 1:
        elif next_blue_value == 3:
        elif next_blue_value == 4:
            if result == -1 or result < input_depth + 1:
                result = input_depth + 1

        print()

    next_depth = input_depth + 1
    for dir_idx in range(len(dh)):
        if dir_idx == input_dir_idx:
            continue
        saved_point_list.append(copy.deepcopy(point_list))
        dfs(next_depth, dir_idx)
        saved_point = saved_point_list.pop()


n, m = map(int, input().split())
my_list = []
depth_max = 10
point_list = [[0, 0], [0, 0]]  # 파랑, 빨강
result = -1
for i in range(n):
    temp_str = input()
    temp_list = []
    for _str in temp_str:
        if _str == "#":
            temp_list.append(1)
        elif _str == "B":
            temp_list.append(2)
            point_list[0] = [i, temp_str.index(_str)]
        elif _str == "R":
            temp_list.append(3)
            point_list[1] = [i, temp_str.index(_str)]

        elif _str == ".":
            temp_list.append(0)
        elif _str == "O":
            temp_list.append(4)
    my_list.append(temp_list)
saved_point_list = []
dfs(-1, -1)
print(result + 1)
