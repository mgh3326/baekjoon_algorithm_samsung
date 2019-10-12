import sys

sys.stdin = open("./data/input.txt")

n_len, m_len = map(int, input().split())
m_list = []
for i in range(m_len):
    temp_list = list(map(int, input().split()))
    m_list.append(temp_list)
result = int((n_len * (n_len - 1) * (n_len - 2)) / 6)
temp_value = (n_len - 2) * m_len
temp_set = set()
value_dict = {}
for m in m_list:
    count = 0
    for i in m:
        if i not in value_dict:
            value_dict[i] = 0
        count += value_dict[i]
        value_dict[i] += 1
    temp_value -= count

print(result - temp_value)
