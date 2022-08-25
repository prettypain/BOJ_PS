'''
문자열이 홀수인 경우에는( aba ) 는 중앙에 b는 무시하고 a 와 a만 비교해서 팰린드롬인지
확인한다. 즉,
길이가 홀수일 때
    (앞 문자열) = string[0:len(string)//2]
    (뒤 문자열) = string[len(string)//2+1:0][::-1]
길이가 짝수일 때
    (앞 문자열) = string[0:len(string)//2]
    (뒤 문자열) = string[len(string)//2:0][::-1]
이라는 식이 나온다.
줄이면
(앞),(뒤) = target[:l//2], target[l//2+(1 if l%2!=0 else 0):][::-1]
가 된다.( [::-1]은 [시작 : 끝 : 단계], range의 파라미터와 유사하다)
또한 두 문자열을 붙였을 때 팰린드롬인지를 구할 때
두가지 경우가 나온다는걸 유의하면 쉽게 풀 수 있다.
a + b 와 b + a는 여기서는 다른 답을 준다.
'''
from sys import stdin
def is_pil(target):
    l = len(target)
    a,b = target[:l//2], target[l//2+(1 if l%2!=0 else 0):][::-1]
    return a==b
input = stdin.readline
for _ in range(int(input())):
    res = 0
    lst = [input().rstrip() for i in range(int(input()))]
    for i in lst:
        tmp = lst.copy()
        tmp.remove(i)
        for j in tmp:
            res = i+j if is_pil(i+j) else j+i if  is_pil(j+i) else 0
            if res: break
        if res: break
    print(res)