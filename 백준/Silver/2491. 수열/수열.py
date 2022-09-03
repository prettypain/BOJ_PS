'''
내가 푼 코드는 O(2N) 즉 O(N)이다. (2는 없애고 표기함)
O(N) 코드는 아마 tmp를 0번째부터 시작하는 값과 -1부터 시작하는 값을 기준으로 하면 가능할 듯하다.

내 코드의 풀이는 아래와 같다.
먼저 입력받은 리스트를 tmp라 하겠다.
O(2N)이라고 말한 이유는 tmp와 뒤집은 tmp로 반복하므로 2N이라고 했다.(N덩이리를 2번해서)
현재 위치에 있는 수와 이전 위치에 있는 수를 비교해서 plus인지 minus인지 체크하고
이전수 대비 증가한다면
--minus를 res에 추가하면서 minus를 1로 초기화 해준다. 이후 plus 1추가

이전수 대비 감소한다면
--plus를 res에 추가하고 plus를 1로 초기화. 이후 minus 1추가
tmp, tmp[::-1](요건 tmp의 시작부터 끝까지 -1만큼 이동한다는 의미 즉 뒤집기)를 반복하면서
최종적인 plus와 minus를 추가하는 코드를 넣어야 한다(증감 체크할 때만 추가하기 때문에)

최최종적으로 max(res)해준다
'''
from sys import stdin
n = int(stdin.readline())
tmp = list(map(int, stdin.readline().split()))
res = tmp[0] if n==1 else 0
for lst in [tmp, tmp[::-1]]:
    plus, minus, before = 1, 1, lst[0]
    for i in lst[1:]:
        if before <= i:
            if minus > res: res = minus
            plus += 1
            minus = 1
        elif before >= i:
            if plus > res: res = plus
            minus += 1
            plus = 1
        before = i
    m = max(plus,minus)
    if m > res: res = m
print(res)