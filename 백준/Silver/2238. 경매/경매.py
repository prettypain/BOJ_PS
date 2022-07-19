u,n = map(int, input().split())
dic = {}
for _ in range(n):
    name, price = input().split()
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