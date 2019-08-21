import sys


def solution():
    n, m = map(int, input().split())
    my_list = []
    for i in range(n):
        temp_str = input()
        my_list.append(temp_str)
    print(my_list)
    return 1


sys.stdin = open("./data/input1.txt", "r")
a = open("./data/output1.txt", "r").read()
print(solution() == a)

print(a)
