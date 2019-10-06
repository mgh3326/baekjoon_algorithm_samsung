import sys

sys.stdin = open("./data/input.txt")

n_len, m_len = map(int, input().split())
value_dict = {}
for i in range(m_len):
    first, second = sorted(list((map(int, input().split()))))
    if first not in value_dict:
        value_dict[first] = set()
    value_dict[first].add(second)
result = 0
for i in range(n_len):
    first = i + 1
    for j in range(first, n_len):
        second = j + 1
        if first in value_dict:
            if second in value_dict[first]:
                continue
        for k in range(second, n_len):
            third = k + 1
            if second in value_dict:
                if third in value_dict[second]:
                    continue
            if first in value_dict:
                if third in value_dict[first]:
                    continue
            result += 1
print(result)
