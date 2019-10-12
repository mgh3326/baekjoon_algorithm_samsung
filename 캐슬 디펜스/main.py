import sys

sys.stdin = open("./data/input.txt")
n, m, d = map(int, input().split())
board_list = []
for i in range(n):
    temp_list = list(map(int, input().split()))
    board_list.append(temp_list)
print()
