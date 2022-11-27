'''
문제의 핵심은 치킨을 먹으면 무족건 쿠폰을 준다는 사실이다.
도장으로 치킨을 먹어도 도장을 준다. (n=1 and k=1이면 무한 치킨 쌉가능)

처음 쿠폰의 갯수(n)은 쿠폰으로 받을 도장의 갯수와 같으므로 도장=쿠폰의 갯수로 시작
그리고 도장을 k로 나눈 몫만큼 주문하고 그 횟수만큼 도장에 추가하는 방식으로 문제 해결

예시
5 2

쿠폰이 5장이므로 5번 먹는다.
count = 5
5번 먹은 것으로 인해 도장이 5회 적립된다.
stamp = 5

k가 2이므로 도장 2개당 치킨 한마리 구매 가능
즉 도장을 k로 나눈 몫만큼 치킨 구매 가능이면서 그 치킨 갯수만큼 도장이 적립됨
count = 5 + 2
stamp = 5%k(치킨 구매로 인한 감소) + 2(치킨 구매로 인한 도장)

도장으로 치킨이 구매 가능(stamp//k가 0보다 크다)이므로 stamp//k만큼 구매
count = 5 + 2 + 1
stamp = 3%k(치킨 구매로 인한 감소) + 1(치킨 구매로 인한 도장)

다시 도장으로 치킨이 구매 가능(stamp//k가 0보다 크다)이므로 stamp//k만큼 구매
count = 5 + 2 + 1 + 1
stamp = 2%k(치킨 구매로 인한 감소) + 1(치킨 구매로 인한 도장)

이제 더이상 치킨 구매가 불가능하다.
최종적으로
count = 9
stamp = 1
이므로 정답은 9가 된다.

대충 이런식으로 문제를 해결했다.
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write
while True:
    try:
        n, k = map(int, input().split())
        stamp = n #도장
        count = n  #치킨 먹은 횟수
        while stamp//k>0:
            t = stamp//k
            stamp = (stamp%k) + t
            count += t
        print(f'{count}\n')
    except:
        break