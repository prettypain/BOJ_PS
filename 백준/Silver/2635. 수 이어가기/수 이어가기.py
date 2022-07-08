n = int(input())
dic = {}
for i in range(n,0,-1):
    List = [n,i]
    while 1:
        t = List[-2] - List[-1]
        if t<0: break
        List.append(t)
    dic[len(List)] = List
t = dic[max(dic.keys())]
print(f'{len(t)}\n'+' '.join(map(str,t)))
