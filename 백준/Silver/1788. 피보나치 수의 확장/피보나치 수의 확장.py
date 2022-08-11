'''
fibo(1), fibo(0)은 각각 1과 0이라고 가정할 때
fibo(1) = 1 = fibo(0) + fibo(-1)
fibo(0) = 0 = fibo(-1) + fibo(-2) = 1 + (-1)

아래와 같은 결과가 나온다.
fibo(n) = res = fibo(n-1) + fibo(n-2)
fibo(-1) = 1 = fibo(-2) + fibo(-3) = -1 + 2
fibo(-2) = -1 = fibo(-3) + fibo(-4) = 2 + (-3)
fibo(-3) = 2 = fibo(-4) + fibo(-5) = -3 + 5
fibo(-4) = -3 = fibo(-5) + fibo(-6) = 5 + (-8)
fibo(-5) = 5 = fibo(-6) + fibo(-7) = -8 + 13
fibo(-6) = -8 = fibo(-7) + fibo(-8) = 13 + (-21)

그리고 이때
fibo(n)의 결과 값과 fibo(-n)의 절대값이 같다는 규칙이 있다.
규칙1 :    fibo(n) == abs(fibo(-n))

또한 n에 따른 fibo(n)의 결과값을 보면 n이 짝수(2로 나누었을때 나머지가 0인경우)인 경우에는
결과값이 음수이고 n이 홀수인 경우에는 결과값이 양수인 것을 알 수 있다.
규칙2 : n이 짝수면 결과는 음수, n이 홀수면 결과는 양수

즉 output결과 "첫째 줄에 F(n)이 양수이면 1, 0이면 0, 음수이면 -1을 출력"출력 요건을
짝수면 -1을 홀수면 1을 0이면 0을 출력하는 형태로 답을 구할 수 있다.

그리고 "둘째 줄에는 F(n)의 절댓값을 출력"둘째 줄 같은 경우는 그냥 피보함수 돌린 결과만 출력
하면 그만이다(규칙 1 참고)
'''
from sys import stdin
def fibo(n):#피보나치수열 for버전
    '''
    재귀버전도 있지만 재귀는 깊이(자기 자신을 불러올 수 있는 횟수)가 어느정도 제한이 있기 때문에
    재귀보다 빠르고 안정성있음 그리고 구현이 상대적으로 쉬움(무슨 지네인지 비네인지 하는 공식으로 구현가능)

    이 함수의 특징을 조금 설명해보기 전에 fibo(3)은 fibo(2)와 fibo(1)로 구할 수 있다.
    그리고 fibo(1)과 fibo(2)는 값이 1이다.
    그러므로 함수에 들어오는 n의 값이 3작으면 1또는 0을 돌려준다(할줄로 처리할려고 머리를 조금 썼다
    그리고 문제에서 "절댓값을 1,000,000,000으로 나눈 나머지를 출력"이라는 문구가 있다
    최종적으로 나누어도 괜찮지만 속도를 위해서 계산할 때 마다 나누었다(나도 몰랐는데 이거 아주 더 더더더더더 빠르다)
    '''
    memo = [1,1]
    if n<3:return n + (-1 if n==2 else 0)
    else:
        for i in range(n-2):
            memo.append((memo.pop(0)+memo[0])%1000000000)
        return memo[1]

n = int(stdin.readline())
print(f'{1 if n>0 else 0 if n==0 else -1 if n%2==0 else 1}\n{fibo(abs(n))}')