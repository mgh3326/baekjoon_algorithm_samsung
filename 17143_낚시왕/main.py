import sys

sys.stdin = open("./data/input.txt")

dir_dict = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, 1],
    4: [0, -1],
}
result = 0
R, C, M = map(int, input().split())
board_list = []
for h in range(R + 1):
    temp_list = [-1] * (C + 1)
    board_list.append(temp_list)
shark_dict = {}
for i in range(M):
    r, c, s, d, z = (map(int, input().split()))
    board_list[r][c] = z
    shark_dict[z] = [r, c, s, d]
current_person_idx = 0
while True:
    # 오른쪽으로 한번 가자
    current_person_idx += 1
    if current_person_idx > C:
        break
    # 상어 잡자
    for _h in range(R):
        h = _h + 1
        if board_list[h][current_person_idx] != -1:
            result += board_list[h][current_person_idx]
            shark_dict.pop(board_list[h][current_person_idx])
            board_list[h][current_person_idx] = -1
            break
    # 상어 움직인다
    # 원래 위치 지우기
    remove_list = []
    for shark_dict_key in shark_dict.keys():
        r, c, s, d = shark_dict[shark_dict_key]
        board_list[r][c] = -1
    for shark_dict_key in shark_dict.keys():
        r, c, s, d = shark_dict[shark_dict_key]
        dh, dw = dir_dict[d]
        for i in range(s):
            r = dh + r
            c = dw + c
            if r <= 0 or c <= 0 or r > R or c > C:
                if d % 2 == 0:
                    d -= 1
                else:
                    d += 1
                dh, dw = dir_dict[d]
                r = dh * 2 + r
                c = dw * 2 + c
        shark_dict[shark_dict_key] = r, c, s, d
        if board_list[r][c] == -1:
            board_list[r][c] = shark_dict_key
        else:
            if board_list[r][c] > shark_dict_key:
                remove_list.append(shark_dict_key)
            else:
                remove_list.append(board_list[r][c])
                board_list[r][c] = shark_dict_key
    for remove in remove_list:
        shark_dict.pop(remove)
print(result)
