import sys

sys.stdin = open("./data/input.txt")
dh = [-1, 1, 0, 0]  # 상 하 좌 우
dw = [0, 0, -1, 1]  # 상 하 좌 우


def is_down(_temp_dict):
    if len(_temp_dict) == 0:
        return False
    for _w in _temp_dict.keys():
        _h = _temp_dict[_w]
        _nh = _h + 1
        if _nh >= r:
            return False
        if board_list[_nh][_w] == 'x':
            return False
    return True


def print_board():
    for board in board_list:
        print(str.join("", board))


def find_low(input_set_index):
    my_dict = {}
    input_set = cluster_list[input_set_index]
    for (_h, _w) in list(input_set):
        if _w not in my_dict:
            my_dict[_w] = _h
        else:
            if _h > my_dict[_w]:
                my_dict[_w] = _h
    if is_down(my_dict):
        out_set = set()
        while True:
            if len(input_set) == 0:
                break
            _h, _w = input_set.pop()
            out_set.add((_h + 1, _w))
            board_list[_h][_w] = "."
            cluster_dict.pop((_h, _w))
        # 가능한 set 만들기
        possible_set = set()
        for out_set_value in list(out_set):
            (_h, _w) = out_set_value
            cluster_dict[(_h, _w)] = input_set_index
            board_list[_h][_w] = "x"
            for _dir_idx in range(len(dh)):
                _nh = dh[_dir_idx] + _h
                _nw = dw[_dir_idx] + _w
                if _nh < 0 or _nw < 0 or _nh >= r or _nh >= c:
                    continue
                possible_set.add((_nh, _nw))

        cluster_list[input_set_index] = out_set

        # merge
        my_dict = {}
        input_set = cluster_list[input_set_index]
        for (_h, _w) in list(input_set):
            if _w not in my_dict:
                my_dict[_w] = _h
            else:
                if _h > my_dict[_w]:
                    my_dict[_w] = _h
        if not is_down(my_dict):
            for cluster_index in range(len(cluster_list)):
                if cluster_index == input_set_index:
                    continue
                current_cluster = cluster_list[cluster_index]
                if len(possible_set.intersection(current_cluster)) != 0:
                    cluster_list[input_set_index] = cluster_list[input_set_index].union(current_cluster)
                    while True:
                        if len(current_cluster) == 0:
                            break
                        pop = current_cluster.pop()
                        cluster_dict[pop] = input_set_index

        find_low(input_set_index)


r, c = map(int, input().split())
board_list = []
cluster_list = []
cluster_dict = {}
temp_set = set()
for h in range(r):
    temp = input()
    for w in range(c):
        c_ = temp[w]
        if c_ == 'x':
            temp_set.add((h, w))
            cluster_dict[(h, w)] = 0

    board_list.append(list(temp))
cluster_list.append(temp_set)
n = int(input())
poll_height_list = list(map(int, input().split()))
# 처음에 분할해주는 과정이 요구되겠다.
# current_cluster_set = cluster_list[0]
# while True:
#     visit_set = set()
#     if len(current_cluster_set) == 0:
#         # cluster_list.pop(current_cluster_index) # 지우면 복잡해지겠다
#         break
#     pop_point = current_cluster_set.pop()
#     current_cluster_set.add(pop_point)
#     queue = [pop_point]
#     while True:
#         if len(queue) == 0:
#             break
#         (h, w) = queue.pop(0)
#         if (h, w) in visit_set:
#             continue
#         visit_set.add((h, w))
#         for dir_idx in range(len(dh)):
#             nh = h + dh[dir_idx]
#             nw = w + dw[dir_idx]
#             if nh >= r or nw >= c or nh < 0 or nw < 0:
#                 continue
#             if board_list[nh][nw] == "x":
#                 queue.append((nh, nw))
#     if len(current_cluster_set) == len(visit_set):
#         break
#     else:
#         current_cluster_set.difference_update(visit_set)
#         cluster_list.append(visit_set)
#         cluster_list_index = len(cluster_list) - 1
#         # 내리기가 필요로함 (w별로 h의 최대값을 찾아야한다.)
#         for (h, w) in list(visit_set):
#             cluster_dict[(h, w)] = cluster_list_index

current_dir = 1
for poll_height in poll_height_list:
    current_h = r - poll_height
    if current_dir == 1:
        current_w = 0
    else:
        current_w = c - 1
    while True:
        if current_w >= c or current_w < 0:
            break
        if board_list[current_h][current_w] == 'x':
            board_list[current_h][current_w] = '.'
            # 값 제거
            current_point = (current_h, current_w)
            current_cluster_index = cluster_dict[current_point]
            cluster_dict.pop(current_point)
            current_cluster_set = cluster_list[current_cluster_index]
            current_cluster_set.remove(current_point)

            # 클러스터가 분할 되었는지 확인하도록 하자
            visit_set = set()
            if len(current_cluster_set) == 0:
                # cluster_list.pop(current_cluster_index) # 지우면 복잡해지겠다
                break
            pop_point = current_cluster_set.pop()
            current_cluster_set.add(pop_point)
            queue = [pop_point]
            while True:
                if len(queue) == 0:
                    break
                (h, w) = queue.pop(0)
                if (h, w) in visit_set:
                    continue
                visit_set.add((h, w))
                for dir_idx in range(len(dh)):
                    nh = h + dh[dir_idx]
                    nw = w + dw[dir_idx]
                    if nh >= r or nw >= c or nh < 0 or nw < 0:
                        continue
                    if board_list[nh][nw] == "x":
                        queue.append((nh, nw))
            if len(current_cluster_set) == len(visit_set):
                pass
            else:
                current_cluster_set.difference_update(visit_set)
                cluster_list.append(visit_set)
                cluster_list_index = len(cluster_list) - 1
                # 내리기가 필요로함 (w별로 h의 최대값을 찾아야한다.)
                for (h, w) in list(visit_set):
                    cluster_dict[(h, w)] = cluster_list_index
                find_low(cluster_list_index)
                find_low(current_cluster_index)

            break

        current_w += current_dir
    current_dir *= -1

print_board()
