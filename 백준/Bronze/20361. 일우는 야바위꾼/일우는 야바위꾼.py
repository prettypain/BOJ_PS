'''
이 문제는 생각보다 쉽다.
그냥 현재 위치 값이 두 입력갑중에 하나라도 해당되면
두 입력값들중에서 현재값이 아닌 값의 값으로 계속 바꿔주면 해결된다.
'''
import sys
input = sys.stdin.readline
n, x, k = map(int, input().split())
for _ in range(k):
    a,b = map(int, input().split())
    x = a if b==x else b if a==x else x
print(x)