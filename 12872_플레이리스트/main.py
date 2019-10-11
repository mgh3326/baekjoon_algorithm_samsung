import sys

sys.stdin = open("input.txt")


# B: 이미 구한 부분 문제의 해를 저장
def bino2(n, k):
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    return B[n][k]


def solution(input_n):
    temp_result = 0
    memo = []
    for i in range(p):
        memo.append(dict())
    if m == 0:
        temp_result = pow(input_n, p)
    else:
        memo[0][(tuple([0]))] = 1
        for i in range(p - 1):
            for memo_tuple in memo[i].keys():
                for j in range(input_n):
                    if j not in memo_tuple:
                        memo_list = list(memo_tuple)
                        memo_list.append(j)
                        if len(memo_list) > m:
                            memo_list.pop(0)
                        if tuple(memo_list) not in memo[i + 1]:
                            memo[i + 1][tuple(memo_list)] = 0
                        memo[i + 1][tuple(memo_list)] += memo[i][memo_tuple]
        for memo_tuple in memo[p - 1].keys():
            temp_result += memo[input_n - 1][memo_tuple]
        temp_result *= input_n
    return temp_result


n, m, p = map(int, input().split())
B = []
for i in range(100):
    temp_list = []
    for j in range(100):
        temp_list.append(list())
    B.append(temp_list)
result = solution(n)
for i in range(n-1):
    result -= solution(i+1) * (bino2(n, i + 1))
print(result)
