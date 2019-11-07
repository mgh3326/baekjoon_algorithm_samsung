# (해결) next_permuations 재귀 사용하지 않고 이용하면 효율적일거 같다
# 다음순열 구하기
def next_permutations(a):
    # i찾기
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    # 마지막 순열인 경우 다음순열이 없으므로 False 반환
    if i == 0:
        return False

    # j찾기
    j = len(a) - 1
    while j > 0 and a[i - 1] >= a[j]:
        j -= 1

    # a[i-1]와 a[j]를 바꾸기
    a[i - 1], a[j] = a[j], a[i - 1]

    # 내림차순을 오름차순으로 정렬하기
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


# 입력받기
num = int(input())
n = list(map(int, input().split()))
a = list(map(int, input().split()))
arr = [0] * a[0] + [1] * a[1] + [2] * a[2] + [3] * a[3]

ans = []

# 로직수행
while True:
    result = 0

    if arr[0] == 0:
        result = n[0] + n[1]
    elif arr[0] == 1:
        result = n[0] - n[1]
    elif arr[0] == 2:
        result = n[0] * n[1]
    else:
        result = n[0] // n[1]

    if len(n) == 2:
        ans.append(result)
        break

    for i in range(2, len(n)):
        if arr[i - 1] == 0:
            result = result + n[i]
        elif arr[i - 1] == 1:
            result = result - n[i]
        elif arr[i - 1] == 2:
            result = result * n[i]
        else:
            if result < 0:
                result = abs(result) // n[i]
                result = -(result)
                continue
            result = result // n[i]
    ans.append(result)

    if next_permutations(arr) == False:
        break

# 결과출력
print(max(ans))
print(min(ans))
