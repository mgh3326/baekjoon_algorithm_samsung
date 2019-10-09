import sys

sys.stdin = open("input.txt")
n = 30
memo = []
for i in range(n * 2):
    temp_list = []
    for j in range(n + 1):
        temp_list.append([0] * (n + 1))
    memo.append(temp_list)
#  depth, 총 알약 갯수, 반쪽 갯수
memo[0][n][0] = 1

for i in range(n * 2 - 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if j >= 0 and k + 1 <= n:
                memo[i + 1][j - 1][k + 1] += memo[i][j][k]
            if k >= 0 and j + 1 <= n:
                memo[i + 1][j + 1][k - 1] += memo[i][j][k]
while True:
    result = 0
    int_n = int(input())
    if int_n == 0:
        break
    for temp_list in memo[2 * int_n - 1]:
        result += temp_list[1]
    print(result)
