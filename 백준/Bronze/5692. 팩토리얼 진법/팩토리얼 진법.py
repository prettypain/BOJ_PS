'''
원래 2진법에서 10진법으로 바꾸는 방법은
1001을 예로 들어 설명하면

1*(2**3) + 0*(2**2) + 0*(2**1) + 1*(2**0)
즉 지수가 왼쪽부터 오른쪽으로 감소하는걸 볼 수 있다.
이걸 뒤집으면 0부터 상승하는걸 볼 수 있다.(더하기는 위치를 바꿔도 괜찮)

그리고 이 문제는 팩토리얼 진법으로 지수를 팩토리얼로 바꾸면 된다.
팩토리얼은 1부터 나 자신까지의 곱으로 표현할 수 있다.
나머지는 구현하면 된다.
'''
from sys import stdin
input = stdin.readline
def fac(n):
    for i in range(n-1, 1, -1):n*=i
    return n
while(target:=input().rstrip())!="0":
    print(sum([int(val)*fac(idx+1) for idx, val in enumerate(target[::-1])]))