'''
문제를 이해했다는 전제 하에 진행.

먼저 이 문제의 핵심은
문자열을 잘 처리해서 그안에 UCPC가 있는지 없는지를 체크하는 것이 중요한 포인트다
그리고 UCCCCCCCCCCCCCCCADADADADAPC 또한 love UCPC이다.
여기서 중요한 부분이 있는데 문자열을 지울 수는 있지만 위치를 교환할 수는 없다
즉 CUPC는 hate UCPC이다. (C와 U의 위치만 바꾸면 love UCPC이지만 바꾸는건 금지)

u, c(1), p, c(2) 각각의 불린 변수를 통해 체크하기로 했다.
c(1)같은 경우 앞서 U가 트루인 경우 즉 이전에 나왔던 경우이면서 C이면서 현제 내 값이 거짓인 경우
에만 c(1)를 true로 바꿀 수 있다.
이런 방식으로 앞에 것이 이미 체크 되었을 때만 이라는 조건을 추가해주면 문제를 쉽게 해결
할 수 있다.
'''
import sys
u,c1,p,c2 = 0,0,0,0
for i in sys.stdin.readline().rstrip():
    if i=="U" and not u:
        u = 1
    elif i=="C" and u and not c1:
        c1 = 1
    elif i=="P" and c1 and not p:
        p = 1
    elif i=="C" and p and not c2:
        c2 = 1
print(f'I {"love UCPC" if u and c1 and p and c2 else "hate UCPC"}')