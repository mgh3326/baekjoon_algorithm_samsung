import sys

sys.stdin = open("./data/input.txt")


# (해결) 시간 초과 ( 0% -> 결과값이 3 이상 나오지 않음을 확인 못 함 , 9% -> 결과값 3 초과 -1이 변경), -> 사다리 타기를 dp로 해보았지만 9% 실패
# 12 번째줄 memo dict를 사용하면 시간 초과가 나오네

def find_combination(_depth, _start_idx):
    global result
    if _depth == size:
        # memo_dict = {}
        for start_idx in range(N):
            current_idx = start_idx
            for h in range(H):
                if current_idx < N - 1 and board_list[h][current_idx]:
                    current_idx += 1
                elif current_idx > 0 and board_list[h][current_idx - 1]:
                    current_idx -= 1
                # if (h, current_idx) not in memo_dict:
                #     memo_dict[h, current_idx] = start_idx
                # else:
                #     current_idx = memo_dict[h, current_idx]
                #     break
            if start_idx != current_idx:
                break
            if start_idx == N - 1:
                if result == -1 or result > size:
                    result = size
        return
    for _idx in range(_start_idx, len(possible_list)):
        if len(combination) != 0 and (
                combination[-1][0] == possible_list[_idx][0] and combination[-1][1] == possible_list[_idx][1] - 1):
            continue
        board_list[possible_list[_idx][0]][possible_list[_idx][1]] = True
        combination.append(possible_list[_idx])
        find_combination(_depth + 1, _idx + 1)
        if result != -1:
            return
        board_list[possible_list[_idx][0]][possible_list[_idx][1]] = False
        combination.pop()


N, M, H = map(int, input().split())
board_list = []
possible_list = []
for i in range(H):
    temp_list = [False] * (N - 1)
    board_list.append(temp_list)
for i in range(M):
    a, b = map(int, input().split())
    board_list[a - 1][b - 1] = True
for i in range(H):
    for idx in range(N - 1):
        if idx < N - 1 and board_list[i][idx]:
            continue
        if idx > 0 and board_list[i][idx - 1]:
            continue
        if idx < N - 2 and board_list[i][idx + 1]:
            continue
        possible_list.append((i, idx))
result = -1
# 0 -> 1 -> 2 -> 3 가능한 조합을 작은순으로 만들어서 종료되면 결과값 return 되도록 하자
# 가능한 조합을 미리 만들자
combination_list = []
for size in range(4):
    combination = []
    find_combination(0, 0)
    if result != -1:
        break
print(result)
