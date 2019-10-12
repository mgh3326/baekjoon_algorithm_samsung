import sys

sys.stdin = open("./data/input.txt")

F, S, G, U, D = map(int, input().split())
visit_list = [False] * F
dest_index = G - 1
depth = 0
queue = []
current_index = S - 1
visit_list[current_index] = True
queue.append([current_index, depth])

while True:
    if len(queue) == 0:
        print("use the stairs")
        break
    current_index, depth = queue.pop(0)
    if current_index == dest_index:
        print(depth)
        break
    next_up_index = current_index + U
    next_down_index = current_index - D
    if next_up_index < 0 or next_up_index >= F:
        pass
    else:
        if visit_list[next_up_index] == False:
            visit_list[next_up_index] = True
            queue.append([next_up_index, depth + 1])
    if next_down_index < 0 or next_down_index >= F:
        pass
    else:
        if visit_list[next_down_index] == False:
            visit_list[next_down_index] = True
            queue.append([next_down_index, depth + 1])
