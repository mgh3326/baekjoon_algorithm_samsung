import sys

sys.stdin = open("./data/input.txt")
n = int(input())
board_list = [list(map(int, input().split())) for i in range(n)]
result = -1
memo_list = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        temp_sum = 0
        for k in range(i + 1):
            for l in range(j + 1):
                memo_list[i][j] += board_list[k][l]

for start_h in range(n):
    for start_w in range(n):
        for d1 in range(1, n + 1):  # 루프 이만큼만 돌면 되려나
            h1, w1 = start_h - d1, start_w + d1  # 첫번째
            if h1 < 0 or h1 >= n or w1 < 0 or w1 >= n:
                break  # 위 조건이라면 더 값이 커지면 안되는게 당연하므로
            for d2 in range(1, n + 1):
                h2, w2 = h1 + d2, w1 + d2  # 두번째
                if h2 < 0 or h2 >= n or w2 < 0 or w2 >= n:
                    break  # 위 조건이라면 더 값이 커지면 안되는게 당연하므로
                h3, w3 = h2 + d1, w2 - d1  # 세번째
                if h3 < 0 or h3 >= n or w3 < 0 or w3 >= n:
                    break  # 위 조건이라면 더 값이 커지면 안되는게 당연하므로
                temp_sum = 0
                temp_count = 1
                rect1_sum = memo_list[start_h - 1][w1]
                rect2_sum = memo_list[h2][n - 1] - memo_list[h2][w1]
                rect3_sum = memo_list[n - 1][w3 - 1] - memo_list[start_h - 1][w3 - 1]
                rect4_sum = memo_list[n - 1][n - 1] - memo_list[n - 1][w3 - 1] - memo_list[h2][n - 1] + memo_list[h2][
                    w3 - 1]
                for r in range(h1, start_h):
                    for i in range(temp_count):
                        c = w1 - i
                        temp_sum += board_list[r][c]
                    temp_count += 1
                rect1_sum -= temp_sum
                temp_sum = 0
                temp_count = 1
                for r in range(h1 + 1, h2 + 1):
                    for i in range(temp_count):
                        c = w1 + i + 1
                        temp_sum += board_list[r][c]
                    temp_count += 1
                rect2_sum -= temp_sum
                temp_sum = 0
                temp_count = 1

                for r in reversed(range(start_h, h3)):
                    for i in range(temp_count):
                        c = w3 - i - 1
                        temp_sum += board_list[r][c]
                    temp_count += 1
                rect3_sum -= temp_sum
                temp_sum = 0
                temp_count = 1
                for r in reversed(range(h2 + 1, h3 + 1)):
                    for i in range(temp_count):
                        c = w3 + i
                        temp_sum += board_list[r][c]
                    temp_count += 1
                rect4_sum -= temp_sum
                center_sum = memo_list[n - 1][n - 1] - rect1_sum - rect2_sum - rect3_sum - rect4_sum
                value = max(rect1_sum, rect2_sum, rect3_sum, rect4_sum, center_sum) - min(rect1_sum, rect2_sum,
                                                                                          rect3_sum,
                                                                                          rect4_sum, center_sum)
                if result == -1 or result > value:
                    result = value
print(result)
