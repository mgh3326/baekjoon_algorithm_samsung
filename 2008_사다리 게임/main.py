import sys

sys.stdin = open("./input.txt")

n, m = map(int, input().split())
a, b, x, y = map(int, input().split())
a -= 1
b -= 1
board_list = []
visit_list = []
for _ in range(m):
    board_list.append(int(input()) - 1)
    visit_list.append([-1] * n)
visit_list.append([-1] * n)
start_index = a
board_index = 0
visit_list[board_index][start_index] = 0
queue = []
queue.append([start_index, 0, 0])  # current_index
while True:
    if len(queue) == 0:
        break
    current_index, value, board_index = queue.pop(0)
    # 왼쪽 오른쪽 그리기

    if current_index > 0:
        if visit_list[board_index][current_index - 1] == -1 or visit_list[board_index][current_index - 1] > value + y:
            visit_list[board_index][current_index - 1] = value + y
            queue.append([current_index - 1, value + y, board_index])
    if current_index < n - 1:
        if visit_list[board_index][current_index + 1] == -1 or visit_list[board_index][current_index + 1] > value + y:
            visit_list[board_index][current_index + 1] = value + y
            queue.append([current_index + 1, value + y, board_index])
    if board_index == len(board_list):
        continue
    board_value = board_list[board_index]
    if current_index - 1 == board_value or current_index == board_value:
        if visit_list[board_index + 1][current_index] == -1 or visit_list[board_index + 1][current_index] > value + x:
            visit_list[board_index + 1][current_index] = value + x
            queue.append([current_index, value + x, board_index + 1])
        if current_index - 1 == board_value:
            current_index -= 1
        elif current_index == board_value:
            current_index += 1
    if visit_list[board_index + 1][current_index] == -1 or visit_list[board_index + 1][current_index] > value:
        visit_list[board_index + 1][current_index] = value
        queue.append([current_index, value, board_index + 1])

    # board_index += 1
print(visit_list[m][b])
