import sys

sys.stdin = open("./data/input.txt")


def is_connecting(my_list):
    current_idx = 0
    visit_list = [False] * len(my_list)
    while True:
        if current_idx == len(my_list) - 1:
            break
        current_value = my_list[current_idx]
        next_idx = current_idx + 1
        next_value = my_list[next_idx]
        if abs(next_value - current_value) > 1:
            return False
        if next_value - current_value == 1:  # 다음칸이 우뚝 솓은 경우 (앞에 부분 부터 세워야한다)
            for x in range(X):
                x_ = (current_idx - x)
                if x_ < 0 or my_list[x_] != current_value or visit_list[x_]:
                    return False
                visit_list[x_] = True
        elif next_value - current_value == -1:  # 다음칸이 파인 경우 (뒷 부분을 세워야한다)
            for x in range(X):
                x_ = (next_idx + x)
                if x_ >= len(my_list) or visit_list[x_] or my_list[x_] != next_value:
                    return False
                visit_list[x_] = True
        current_idx = next_idx
    return True


result = 0
N, X = map(int, input().split())
board_list = []
for i in range(N):
    board_list.append(list(map(int, input().split())))
for board in board_list:  # 가로
    if is_connecting(board):
        result += 1
for w in range(N):
    temp_list = []
    for h in range(N):
        temp_list.append(board_list[h][w])
    if is_connecting(temp_list):
        result += 1
print(result)
