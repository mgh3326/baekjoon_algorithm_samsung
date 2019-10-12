import sys

sys.stdin = open("./data/input1.txt", "r")

N = int(input())
my_list = []
save_dict = {}
count = 0
for i in range(N * N - N // 2):
    temp_list = list(map(int, input().split()))
    my_list.append(temp_list)
board_list = []
for i in range(N):
    temp_list = []
    if i % 2 != 0:
        temp_list.append(0)
        for j in range(N - 1):
            temp_list.extend(my_list[count])
            count += 1
        temp_list.append(0)

    else:
        for j in range(N):
            temp_list.extend(my_list[count])
            count += 1
    board_list.append(temp_list)
current_index = 0
queue = []
depth = 0
queue.append([current_index, depth, [1]])
save_dict[current_index] = depth
result = 0
while True:
    if len(queue) == 0:
        break
    current_index, depth, current_list = queue.pop(0)
    if current_index + 1 < len(my_list) and my_list[current_index + 1][0] != 0:
        if my_list[current_index][1] == my_list[current_index + 1][0]:
            if current_index + 1 not in save_dict:
                copy = current_list.copy()
                copy.append(current_index + 1)
                queue.append([current_index + 1, depth + 1, copy])
                save_dict[current_index + 1] = depth + 1
    # 좌 (0, 9,
    # 상 (좌,우)
    # 하 (좌,우)

print()
