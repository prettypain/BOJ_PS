#파이썬의 특징인 슬라이싱한 부분에 값넣는 방법으로 문제해결
n, m = map(int, input().split())
lst = list(range(1, n+1))
for _ in range(m):
    a, b = map(int, input().split())
    lst[a-1:b] = lst[a-1:b][::-1]
print(*lst)