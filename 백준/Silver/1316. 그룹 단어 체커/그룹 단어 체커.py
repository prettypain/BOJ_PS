def f():
#이전 단어와 현재 단어를 비교했을 때 다르면서 이미 한번 나온 단어의 경우
#해당 tmp는 그룹단어가 아니게 된다.
    dic[tmp[0]]=1
    for k in range(1,len(tmp)):
        if tmp[k-1]!=tmp[k] and dic[tmp[k]]==1:
            return 0
        dic[tmp[k]] = 1
    return 1


n = int(input())
resC = 0
for i in range(n):
    dic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
       'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    #매 단어마다 체크리스트를 초기화.
    
    tmp = input()
    if len(tmp) == 1: #입력된 단어가 1자리인 경우에는 모족건 구릅단어이다.
        resC+=1
    else:
        resC += f()
print(resC)
