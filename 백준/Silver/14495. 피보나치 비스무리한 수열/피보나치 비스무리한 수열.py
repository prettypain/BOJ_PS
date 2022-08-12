'''
생각보다 쉽다.
"피보나치 비스무리한 수열"이 조금 재미있다면 "피보나치 수의 확장"이라는 문제를
추천한다.

문제 해결 방법은 간단하다
fibo(1) = fibo(2) = fibo(3) = 1
이라는 가정이 주어진다.
그리고 피보나치를 배웠을 때는 fibo(0) = 0, fibo(1) = 1이라는 가정이 있었다.
그리고 memo = [0,1]로 놓고
n-1회 만큼
memo.append( memo.pop(0) + memo[0] )를 반복했다.

그렇다 우린 가정할때의 값만 달라졌을 뿐 과정은 굉장히 유사하다는 것을 알 수 있다.
이 문제의 피보나치 수를 구하는 방법을 생각해보자.
n=4인 피보나치 수를 구하기 위해서는
fibo(4) = fibo(3) + fibo(1)
이라는 식이 나온다, 즉 memo = [1,1,1] #1번째, 2번째, 3번째 라고할 때
(다음 피보나치 수) = memo[0] + memo[2] 라는 식이 나온다
이걸 조금만 손 봐주면
memo.append(memo.pop(0) + memo[1])로 연결 할 수 있다.
pop(0)을 통해 memo[0]의 역할을 하는 것과 동시 리스트를 효율적(적게)사용할 수 있고
memo[1]은 memo[2]의 역할을 한다 인덱스 값이 다른 이유는 위에서
pop(파라미터 값의 위치한 값을 리턴하고 삭제한다)를 했기 때문에 인덱스가 땡겼기 때문이다.
'''

from sys import stdin
def same_fibo(n):
    memo = [1,1,1]
    for i in range(n-3):
        memo.append(memo.pop(0) + memo[1])
    return memo[2]
print(same_fibo(int(stdin.readline())))