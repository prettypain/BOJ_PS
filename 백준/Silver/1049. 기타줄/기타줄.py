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
print(min(minimum, pack_min*(n//6) + one_min*(n%6), one_min * n, pack_min * (n//6 + (1 if n%6 else 0))))
