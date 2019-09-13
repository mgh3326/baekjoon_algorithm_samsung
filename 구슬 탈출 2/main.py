import sys

sys.stdin = open("./data/my_input1.txt", "r")
# a = open("./data/output1.txt", "r").read()
# print(a)

dh = [-1, 0, 1, 0]  # 상 좌 하 우
dw = [0, -1, 0, 1]  # 상 자 하 우


def run_red(current_red_point, nh, nw, current_blue_point):
    while True:
        next_red_point = current_red_point[0] + nh, current_red_point[1] + nw
        if my_list[next_red_point[0]][next_red_point[1]] == -1:
            break
        elif next_red_point == tuple(current_blue_point):
            break
        elif my_list[next_red_point[0]][next_red_point[1]] == 1:
            return 0
        elif my_list[next_red_point[0]][next_red_point[1]] == 0:
            current_red_point = list(next_red_point)
    return current_red_point


def run_blue(current_blue_point, nh, nw, current_red_point):
    while True:
        next_blue_point = current_blue_point[0] + nh, current_blue_point[1] + nw
        if my_list[next_blue_point[0]][next_blue_point[1]] == -1:
            break
        elif my_list[next_blue_point[0]][next_blue_point[1]] == 1:
            return -1
        elif next_blue_point == tuple(current_red_point):
            break
        elif my_list[next_blue_point[0]][next_blue_point[1]] == 0:
            current_blue_point = list(next_blue_point)
        else:
            pass
    return current_blue_point


n, m = map(int, input().split())
my_list = []
depth_max = 10
point_list = [
    [0, 0], [0, 0]
]

result = -1
for i in range(n):
    temp_str = input()
    temp_list = []
    for _str in temp_str:
        if _str == "#":  # 벽
            temp_list.append(-1)
        elif _str == "B":  # Blue
            temp_list.append(0)
            point_list[1] = [i, temp_str.index(_str)]
        elif _str == "R":
            temp_list.append(0)  # Red
            point_list[0] = [i, temp_str.index(_str)]
        elif _str == ".":  # 움직일수 있는 공간
            temp_list.append(0)
        elif _str == "O":  # 블랙홀
            temp_list.append(1)
    my_list.append(temp_list)
saved_point_set = set()
saved_point_set.add((tuple(point_list[0]), tuple(point_list[1])))  # Red, Blue
queue = [[point_list[0], point_list[1], 0]]

while True:
    if result != -1:
        break
    if len(queue) == 0:
        break
    start_red_point, start_blue_point, depth = queue.pop(0)
    if depth == 10:
        break
    for dir_idx in range(len(dh)):
        nh = dh[dir_idx]
        nw = dw[dir_idx]
        current_red_point = start_red_point.copy()
        current_blue_point = start_blue_point.copy()
        temp_point = current_red_point
        if dir_idx == 0:  # 위일 경우
            temp_point = min(current_red_point, current_blue_point, key=lambda x: x[0])
        if dir_idx == 1:  # 좌일 경우
            temp_point = min(current_red_point, current_blue_point, key=lambda x: x[1])
        if dir_idx == 2:  # 하일 경우
            temp_point = max(current_red_point, current_blue_point, key=lambda x: x[0])
        if dir_idx == 3:  # 우일 경우
            temp_point = max(current_red_point, current_blue_point, key=lambda x: x[1])
        if temp_point == current_red_point:  # 레드 먼저
            current_red_point = run_red(current_red_point, nh, nw, current_blue_point)
            if current_red_point == 0:
                current_blue_point = run_blue(current_blue_point, nh, nw, [0, 0])
                if current_blue_point != -1:
                    result = depth + 1
                    break
            else:
                current_blue_point = run_blue(current_blue_point, nh, nw, current_red_point)
        else:  # 블루 먼저
            current_blue_point = run_blue(current_blue_point, nh, nw, current_red_point)
            if current_blue_point == -1:
                continue
            current_red_point = run_red(current_red_point, nh, nw, current_blue_point)
            if current_red_point == 0:
                result = depth + 1
                break
        if current_blue_point == -1:
            continue
        if (tuple(current_red_point), tuple(current_blue_point)) not in saved_point_set:
            saved_point_set.add((tuple(current_red_point), tuple(current_blue_point)))
            queue.append([current_red_point, current_blue_point, depth + 1])
print(result)
