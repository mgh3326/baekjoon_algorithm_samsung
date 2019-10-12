import sys

sys.stdin = open("input.txt")

input_str = input()
alpha_dict = {
    "B": 0,
    "C": 1
}
alpha_list = ["B", "C"]
m = len(input_str)

result = -1
alpha_count_list = [0] * 2
a_count = 0
queue = []
for i in range(m):
    if input_str[i] == "A":
        a_count += 1
    else:
        alpha_count_list[alpha_dict[input_str[i]]] += 1
total_count = sum(alpha_count_list)
if total_count > a_count + 1:
    pass
else:
    memo = [False] * (a_count + 1)
    queue = []
    for i in range(3):
        if i == 2:
            queue.append((alpha_count_list, " ", total_count))
        else:
            if alpha_count_list[i] != 0:
                copy = alpha_count_list.copy()
                copy[i] -= 1
                queue.append((tuple(copy), alpha_list[i], total_count - 1))
    queue_idx = 0
    while True:
        if queue_idx >= len(queue):
            break
        current_tuple, current_str, current_count = queue[queue_idx]
        if current_count == 0:
            result = ""
            for value in current_str:
                if value == " ":
                    pass
                else:
                    result += value
                result += "A"
            result = result[:-1]
            break
        for i in range(3):
            if i == 2:
                queue.append((current_tuple, current_str + " ", current_count))
            else:
                if current_tuple[i] != 0:
                    alpha_count_list = list(current_tuple)
                    alpha_count_list[i] -= 1
                    queue.append((tuple(alpha_count_list), current_str + alpha_list[i], current_count - 1))
        queue_idx += 1
print(result)
