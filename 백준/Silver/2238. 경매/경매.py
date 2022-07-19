'''
이 문제에서 가장 중요한 부분은
금액이 낮으면서 가장 적은 사람이 참가한 경우에서 먼저 온 사람을 출력해야 한다.
그러므로 가장 사람이 적은 곳의 값을 가지고
값이 낮은 사람부터 찾다보면 이 조건을 만족하는 곳에서 가장 먼저 온 사람을
출력하면 문제는 해결이다.
만약 조건중 하나라도 없으면 ValueError가 나온다. 왜 아냐고? 나도 별로 알고 싶지 않았다.....
'''
import sys
input = sys.stdin.readline
u,n = map(int, input().split())
dic = {}
for _ in range(n):
    name, price = input().rstrip().split()
    price = int(price)
    if price>u: continue
    if dic.get(price): dic[price] += ' '+name
    else: dic[price] = name
tar_min = min(map(lambda x : len(x.split()),dic.values()))
while True:
    m = min(dic.keys())
    tar = dic[m].split()
    if len(tar) > tar_min:
        dic.pop(m)
    else:
        print(tar[0],m)
        break