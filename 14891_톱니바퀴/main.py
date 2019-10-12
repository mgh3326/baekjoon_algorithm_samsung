import sys

sys.stdin = open("./data/input1.txt", "r")

topni_num = 4
topni_list = []
for i in range(topni_num):
    temp = input()
    topni_list.append(list(map(int, temp)))
rotate_num = int(input())


def rotate_topni(current_topni_index, input_topni_dir):
    if input_topni_dir == 1:  # 시계 방향
        _pop = topni_list[current_topni_index].pop()
        topni_list[current_topni_index].insert(0, _pop)
    else:
        _pop = topni_list[current_topni_index].pop(0)
        topni_list[current_topni_index].append(_pop)


# 2
# 6
for i in range(rotate_num):
    topni_index, topni_dir = map(int, input().split())
    if topni_index < topni_num and topni_list[topni_index - 1][2] != topni_list[topni_index][6]:
        if topni_index + 1 < topni_num and topni_list[topni_index][2] != topni_list[topni_index + 1][6]:
            if topni_index + 2 < topni_num and topni_list[topni_index + 1][2] != topni_list[topni_index + 2][6]:
                rotate_topni(topni_index, topni_dir * -1)
                rotate_topni(topni_index + 1, topni_dir)
                rotate_topni(topni_index + 2, topni_dir * -1)
            else:
                rotate_topni(topni_index, topni_dir * -1)
                rotate_topni(topni_index + 1, topni_dir)

        else:
            rotate_topni(topni_index, topni_dir * -1)
    if topni_index - 2 >= 0 and topni_list[topni_index - 1][6] != topni_list[topni_index - 2][2]:
        if topni_index - 3 >= 0 and topni_list[topni_index - 2][6] != topni_list[topni_index - 3][2]:
            if topni_index - 4 >= 0 and topni_list[topni_index - 3][6] != topni_list[topni_index - 4][2]:
                rotate_topni(topni_index - 4, topni_dir * -1)
                rotate_topni(topni_index - 2, topni_dir * -1)
                rotate_topni(topni_index - 3, topni_dir)
            else:
                rotate_topni(topni_index - 2, topni_dir * -1)
                rotate_topni(topni_index - 3, topni_dir)
        else:
            rotate_topni(topni_index - 2, topni_dir * -1)

    rotate_topni(topni_index - 1, topni_dir)
answer = 0
for i in range(topni_num):
    answer += pow(2, i) * topni_list[i][0]
print(answer)
