import sys

sys.stdin = open("input.txt")
N = int(input())
my_list = []
memo = []
memo.append(0)
for i in range(N):
    my_list.append(list(map(int, input().split())))
# 거꾸로 넣자
for i in range(N):
    idx = N - i - 1
    time, profit = my_list[idx]

    if i + 1 - time < 0:
        memo.append(memo[-1])
    else:
        memo.append(max(profit + memo[i + 1 - time], memo[-1]))

print(memo[-1])
