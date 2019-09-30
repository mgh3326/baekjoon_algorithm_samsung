import sys

sys.stdin = open("./data/input1.txt", "r")
board_list = []
n, m, x, y, k = list(map(int, input().split()))
for i in range(n):
    temp_list = list(map(int, input().split()))
    board_list.append(temp_list)
print()
