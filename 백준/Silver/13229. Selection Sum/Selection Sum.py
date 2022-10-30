'''
간단한 누적합 문제
[1, 4, 5] 라는 배열이 있다. 이때 배열에 s~e까지 합을 여러번 구해야 한다면?

i>0 : lst[i] = lst[i] + lst[i-1]
누적합 배열을 먼저 만든다. [0, 1, 5, 6]
그럼 각 인덱스는 자신 이전의 인덱스들의 값을 모두 가지고 있다. 즉
배열 : 가진 인덱스(값)
lst[1] : 1
lst[2] : 1, 2
lst[3] : 1, 2, 3

예를들어 1번째부터 3번째까지의 합을 구해야한다면
lst[3] - lst[0]                ( {1, 2, 3} - {}     == {1, 2, 3} )
예를들어 2번째부터 3번째까지의 합을 구해야한다면
lst[3] - lst[1]                ( {1, 2, 3} - {1}      == {2, 3} )
예를들어 3번째부터 3번째까지의 합을 구해야한다면
lst[3] - lst[2]                ( {1, 2, 3} - {1, 2}     == {3} )


저것이 인덱스의 집합끼리 연결된다고 생각하면 된다.
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
lst = [0] + list(map(int, input().split()))
for i in range(1, n+1): lst[i] += lst[i-1]
for _ in range(int(input())):
    s, e = map(int ,input().split())
    print(f'{lst[e+1] - lst[s]}\n')