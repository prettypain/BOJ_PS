'''
하루에 올라가고 미끄러져 내려오는 것을 고려하면 하루 동안 이동하는 거리는 A - B.
V - B 는 마지막 날에 미끄러져 내려오지 않기 때문에 그 거리를 뺀 거리가 됨.
날짜 를 C라고 했을 때 수식은
(A-B)*(C-1)+A>=V
우리는 언제 도착했는지를 알아야하므로 C에대한 식으로 바꿔준다.
(A-B)*(C-1)+A>=V
AC-A-BC+B+A >= V
AC-BC+B >= V
C*(A-B)+B >= V
C*(A-B) >= V-B
C >= (V-B)/(A-B) 가 결론적으로 성립하게 된다.
또한 V에 도착하는 경우는 항상 낯 즉 하루가 아니다 그러므로 나눈 값의 소수점이 조금이라도
있다면 올림해버린다.

'''
import sys, math
input = sys.stdin.readline
a,b,v = map(int, input().split())
print(math.ceil((v-b)/(a-b)))
