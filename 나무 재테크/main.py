import sys

sys.stdin = open("./data/input8.txt", "r")
board_size, m, k = (map(int, input().split()))
board_list = [[5 for x in range(board_size)] for y in range(board_size)]
winter_list = []
tree_dict = {}
for h in range(board_size):
    temp_list = list((map(int, input().split())))
    winter_list.append(temp_list)
for i in range(m):
    _x, _y, z = (map(int, input().split()))
    x = _x - 1
    y = _y - 1
    if (x, y) not in tree_dict:
        tree_dict[(x, y)] = []
    tree_dict[(x, y)].append(z)
current_time = 0
while True:
    if current_time == k:
        break
    remove_list = []
    create_point_list = []
    # TODO 시간초과로 인해 실패하였다. sort 하지 않고 할수 있는 방법이 있을까? 우선순위 큐를 사용하면 가능해질까?
    # 봄
    for tree_dict_key in tree_dict.keys():
        tree_dict_value_list = tree_dict[tree_dict_key]
        tree_dict_value_list.sort()  # 효율성이 괜찮을까? => 안 괜찮은거 같다.
        for idx, tree_dict_value in enumerate(tree_dict_value_list):
            board_list[tree_dict_key[0]][tree_dict_key[1]] -= tree_dict_value
            if board_list[tree_dict_key[0]][tree_dict_key[1]] < 0:
                board_list[tree_dict_key[0]][tree_dict_key[1]] += tree_dict_value

                remove_list.append([tree_dict_key, tree_dict_value])
            else:

                tree_dict_value_list[idx] += 1
                if tree_dict_value_list[idx] % 5 == 0:
                    create_point_list.append(tree_dict_key)
    # 여름
    for remove in remove_list:
        if len(tree_dict[remove[0]]) == 1:
            tree_dict.pop(remove[0])
        else:
            tree_dict[remove[0]].remove((remove[1]))
        board_list[remove[0][0]][remove[0][1]] += remove[1] // 2
    # 가을
    for create_point in create_point_list:
        h, w = create_point
        if h - 1 < 0 or w - 1 < 0:
            pass
        else:
            if (h - 1, w - 1) not in tree_dict:
                tree_dict[(h - 1, w - 1)] = []
            tree_dict[(h - 1, w - 1)].append(1)
        if h - 1 < 0:
            pass
        else:
            if (h - 1, w) not in tree_dict:
                tree_dict[(h - 1, w)] = []
            tree_dict[(h - 1, w)].append(1)
        if h - 1 < 0 or w + 1 >= board_size:
            pass
        else:
            if (h - 1, w + 1) not in tree_dict:
                tree_dict[(h - 1, w + 1)] = []
            tree_dict[(h - 1, w + 1)].append(1)
        if w - 1 < 0:
            pass
        else:
            if (h, w - 1) not in tree_dict:
                tree_dict[(h, w - 1)] = []
            tree_dict[(h, w - 1)].append(1)
        if w + 1 >= board_size:
            pass
        else:
            if (h, w + 1) not in tree_dict:
                tree_dict[(h, w + 1)] = []
            tree_dict[(h, w + 1)].append(1)
        if h + 1 >= board_size or w - 1 < 0:
            pass
        else:
            if (h + 1, w - 1) not in tree_dict:
                tree_dict[(h + 1, w - 1)] = []
            tree_dict[(h + 1, w - 1)].append(1)
        if h + 1 >= board_size:
            pass
        else:
            if (h + 1, w) not in tree_dict:
                tree_dict[(h + 1, w)] = []
            tree_dict[(h + 1, w)].append(1)
        if h + 1 >= board_size or w + 1 >= board_size:
            pass
        else:
            if (h + 1, w + 1) not in tree_dict:
                tree_dict[(h + 1, w + 1)] = []
            tree_dict[(h + 1, w + 1)].append(1)
    for h in range(board_size):
        for w in range(board_size):
            board_list[h][w] += winter_list[h][w]
    current_time += 1
result = 0
for value in tree_dict.values():
    result += len(value)

print(result)
