'''
그냥 깡으로 문제 풀었습니다.
모든 브랜드에서 패키지만 사는 가격, 낱개만 사는 가격, 패키지와 낱개로 사는 가격의 최소값을
구하고 각 가격을 구하면서 패키지로 살 때 가장 저렴한 가격과 낱개로 살 때 가장 저렴한 가격
즉 같이 입력이 되지 않은 값
ex)
9 10
40 5
라면 패키지 가격으로 9, 낱개 가격으로 5를 가져와 위에서 했던 것처럼 최소값을 구해서
사전에 구한 최소값과 비교해 가장 작은 값을 구함.
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write
#n, m : 끊어진 줄 수, 브랜드 수
n, m = map(int, input().split())
minimum, pack_min, one_min = 10000001, 10000001, 10000001
for i in range(m):
    pack, one = map(int, input().split())
    pack_price = pack * (n//6 + (1 if n%6 else 0))
    one_price = one * n
    pack_and_one_price = pack*(n//6) + one*(n%6)

    temp_min = min(pack_price, one_price, pack_and_one_price)
    if temp_min < minimum: minimum = temp_min
    if pack < pack_min: pack_min = pack
    if one < one_min: one_min = one
print(f'{min(minimum, pack_min*(n//6) + one_min*(n%6), one_min * n, pack_min * (n//6 + (1 if n%6 else 0)))}')