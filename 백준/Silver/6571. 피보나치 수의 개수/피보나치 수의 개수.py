'''
솔직히 이 문제 시간초과 날줄 알고 기대조차 하지 않았다.....ㅎ
처음에 제출했을 때 틀린 부분을 설명해보자면
a,b 범위가 1,2일때(최소의 경우)를 생각하지 않아서 오답떴다(이후 수정후 맞음)

이 문제의 핵심은 bottom-up방식으로 진행해 효율적으로 문제를 해결하면 된다.
그리고 매 증가마다 a<=f(i)<=b 인지 카운팅하고 출력하면 끝이다.
'''
from sys import stdin
while 1:    
    a,b = map(int, stdin.readline().split())
    if a==b==0: break
    memo = [1,2]
    c = 1 if a<=1<=b else 0
    c = c+1 if a<=2<=b else c
    while memo[1]<b:
        memo.append(memo.pop(0) + memo[0])
        if a<=memo[1]<=b:
            c+=1
    print(c)