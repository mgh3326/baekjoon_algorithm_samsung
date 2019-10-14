import sys

sys.stdin = open("./data/input1.txt", "r")

top_num = int(input())
top_list = list(map(int, input().split()))
save_list = []
save_max = 0
result_list = []

for top_index in range(top_num):
    top = top_list[top_index]
    while True:
        if len(save_list) == 0:
            result = 0
            break
        save, result = save_list[-1]
        if save > top:
            break
        else:
            save_list.pop()
    result_list.append(result)
    save_list.append((top, top_index + 1))

for result in result_list:
    print(result, end=" ")
print()
