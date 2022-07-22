'''
문제 풀이법을 간단하게 설명하자면
가장 큰 값의 인덱스가 0이면서 가장 큰 값의 수가 1인 경우가 될 때 까지 아래 과정을 반복
    1. 0번째를 제외한 가장 큰 값의 인덱스를 찾는다(+1한 이유는 슬라이싱을 통해 1번쨰부터 찾았고 결국에는 lst에 접근해야 할 때 위치기 밀리니까 미리 +1해줌)
    2. 가장 큰 값의 위치한 값을 -1해준다.
    3. lst에 0번째와 c변수를 각각 1씩 더해준다.
이후 c를 출
'''
from sys import stdin
input = stdin.readline
c = 0
n = int(input())
lst = [int(input()) for i in range(n)]
while True:
    m = max(lst)
    if lst.index(m)==0 and lst.count(m)==1: break
    lst[lst[1:].index(m)+1]-=1
    lst[0] += 1;c+=1
print(c)
