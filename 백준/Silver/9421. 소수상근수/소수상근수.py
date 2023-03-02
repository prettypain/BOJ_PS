'''
문제의 해결방법은 생각보다 간단하게 생각해 낼 수 있다.
문제는 TLE이지만 다행이 시간은 넉넉했다.

먼저 체를 통해서 n이하의 모든 소수를 구한다.
이후 구한 소수들 중에서 상근수 즉
각 자리수의 제곱의 합을 여러번 계산한 결과가 1이 되는 수를 모두 출력한다.

즉 우리는 sieve와 check_sang 두 함수가 필요하다.
그런데 3의 경우 1이 안나오고 무한히 제곱합을 계산한다.
그런데 이런 경우 제곱합의 값이 루프처럼 다시 반복된다는 특징이 있다.
즉 이전에 제곱합을 계산한 값이 다시 나온다면 그 수는 상근수가 아니다.
이점 유의해서 구현하면 1000ms대 정답을 받을 수 있다.
'''

import sys
def sieve(n):
    arr = list(range(n+1))
    arr[1] = 0
    for i in range(2, int(n**0.5)+1):
        if arr[i] == 0: continue
        for j in range(i+i, n+1, i): arr[j] = 0
    return list(filter(lambda x : x!=0, arr))

def sang(n):
    tmp = []
    while n!=1:
        n = sum(map(lambda x : int(x)**2, str(n)))
        if n in tmp: return False
        else: tmp.append(n)
    return True

n = int(sys.stdin.readline())
lst = sieve(n)
for i in lst:
    if sang(i): sys.stdout.write(f'{i}\n')
