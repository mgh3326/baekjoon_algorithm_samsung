import sys

sys.stdin = open("input.txt")

input_str = input()
alpha_dict = {
    "A": 0,
    "B": 1,
    "C": 2
}
alpha_list = ["A", "B", "C"]
m = len(input_str)

result = -1
alpha_count_list = [0] * 3
queue = []
for i in range(m):
    alpha_count_list[alpha_dict[input_str[i]]] += 1
for i in range(3):
    if alpha_count_list[i] != 0:
        copy = alpha_count_list.copy()
        copy[i] -= 1
        queue.append((tuple(copy), alpha_list[i]))
queue_idx = 0
is_end = False
while True:
    if queue_idx >= len(queue):
        break
    current_alpha_tuple, current_str = queue[queue_idx]
    len_current_str = len(current_str)
    for i in range(3):
        if current_alpha_tuple[i] != 0:
            if i == 1:  # B
                if current_str[-1] == "B":
                    continue
            elif i == 2:  # C
                if current_str[-1] == "C" or (len_current_str >= 2 and current_str[-2] == "C"):
                    continue
            current_alpha_list = list(current_alpha_tuple)
            current_alpha_list[i] -= 1
            next_str = current_str + alpha_list[i]
            if len_current_str + 1 == m:
                result = next_str
                is_end = True
                break
            queue.append((tuple(current_alpha_list), next_str))
    if is_end:
        break
    queue_idx += 1
print(result)
