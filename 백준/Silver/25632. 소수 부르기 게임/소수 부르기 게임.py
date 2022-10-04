'''
2~1000까지의 소수를 구한다고 하면 약 2000번 정도 반복하면 2~1000까지의 소수가 나온다.
그리고 용태랑 유진의 범위에 맞게 소수들을 주고 서로 배틀하게 하면 된다.

배틀은 예시로 설명하겠다.
1. 용태의 턴이다.
 용태가 들고 있는 소수중에서 유진이 들고있는 소수가 있다면? 바로 사용.
 (사용하면 용태꺼 뿐만아니라 유진것도 사라져서 이득)
 용태가 들고있는 소수의 개수가 0개라면 유진의 승리라고 외치고 마친다.

2. 유진이의 턴이다.
 유진이가 들고있는 소수 중에서 용태가 가지고 있는 소수를 찾아봤지만 없다.
 유진은 그냥 아무거나 사용한다.
 유진이 들고있는 소수의 개수가 0개라면 유진의 승리라고 외치고 마친다.

1, 2를 계속 반복하면 된다. 끝~
'''
def sieve(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return lst

lst = sieve(1000)

a, b = map(int, input().split())
c, d = map(int, input().split())

ab = list(filter(lambda x : x!=0, lst[a:b+1]))
cd = list(filter(lambda x : x!=0, lst[c:d+1]))
while True:
    #용태 턴~
    if len(ab)==0: #yt의 소수가 없는 경우
        print("yj")
        break
    s = 1 #하나라도 출력하지 않았는가?에 해당하는 변수(그러면 아무거나 없애려고)
    for i in range(len(ab)):
        if ab[i] in cd:
            cd.pop(cd.index(ab.pop(i)))
            s = 0
            break
    if s:ab.pop(0) #하나라도 출력하지 않은 경우 아무거나 없애기

        
    #유진이 턴~
    if len(cd)==0: #yj의 소수가 없는 경우
        print("yt")
        break
    s = 1 #하나라도 출력하지 않았는가?에 해당하는 변수(그러면 아무거나 없애려고)
    for i in range(len(cd)):
        if cd[i] in ab:
            ab.pop(ab.index(cd.pop(i)))
            s = 0
            break
    if s: cd.pop(0) #하나라도 출력하지 않은 경우 아무거나 없애기