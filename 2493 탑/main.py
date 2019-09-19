import sys

sys.stdin = open("./data/input1.txt", "r")

top_num = int(input())
top_list = list(map(int, input().split()))
save_list = []
save_max = 0
result_list = []

for top_index in range(top_num):
    top = top_list[top_index]
    if top > save_max:
        result_list.append(0)
    else:
        result = 0
        while True:
            save = save_list[top_index - result - 1]
            if save > top:
                result_list.append(top_index - result)
                break
            result += 1

    save_list.append(top)
    if top > save_max:
        save_max = top

for result in result_list:
    print(result, end=" ")
print()
