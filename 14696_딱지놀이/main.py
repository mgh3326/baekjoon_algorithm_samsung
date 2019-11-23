import sys

sys.stdin = open("./data/input.txt")

N = int(input())
for _ in range(N):
    result = "D"
    a_list = list(map(int, input().split()))[1:]
    b_list = list(map(int, input().split()))[1:]
    a_value_list = [0 for _ in range(5)]
    b_value_list = [0 for _ in range(5)]
    for a in a_list:
        a_value_list[a] += 1
    for b in b_list:
        b_value_list[b] += 1
    if a_value_list[4] > b_value_list[4]:
        result = "A"
        print(result)
        continue
    if a_value_list[4] < b_value_list[4]:
        result = "B"
        print(result)
        continue
    if a_value_list[3] > b_value_list[3]:
        result = "A"
        print(result)
        continue
    if a_value_list[3] < b_value_list[3]:
        result = "B"
        print(result)
        continue
    if a_value_list[2] > b_value_list[2]:
        result = "A"
        print(result)
        continue
    if a_value_list[2] < b_value_list[2]:
        result = "B"
        print(result)
        continue
    if a_value_list[1] > b_value_list[1]:
        result = "A"
        print(result)

        continue
    if a_value_list[1] < b_value_list[1]:
        result = "B"
        print(result)
        continue
    print(result)
