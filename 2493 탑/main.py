import sys

sys.stdin = open("./data/input1.txt", "r")
import heapq

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
        copy = save_list.copy()
        result = -1
        while True:
            if len(copy) == 0:
                break
            heappop = heapq.heappop(copy)
            save = heappop[0] * -1
            if save < top:
                break
            if result < heappop[1] + 1:
                result = heappop[1] + 1
        result_list.append(result)
    heapq.heappush(save_list, (top * -1, top_index))
    if top > save_max:
        save_max = top

for result in result_list:
    print(result, end=" ")
print()
