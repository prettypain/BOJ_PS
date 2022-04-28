while True:
    dic = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0
    }
    tmp = input().lower()
    if tmp=="#":break
    for i in ['a', 'e', 'i', 'o', 'u']:
        c = tmp.count(i)
        if c>=1:
            dic[i] += c

    print(sum(dic.values()))
