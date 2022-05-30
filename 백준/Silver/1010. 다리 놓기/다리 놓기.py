'''
#https://www.youtube.com/watch?v=8aJzzwzByLc
고등 수학 확통
nCr = n!/(n-r)! * r!

#https://www.acmicpc.net/board/view/24868
중요한 포인트를 잡아줌
'''
def fac(target):#팩토리얼 함수(재귀보단 속도가 월등히 빠름)
    for i in range(target-1,0,-1):
        target*=i
    return target


for i in range(int(input())):
    r,n = map(int, input().split())
    if r==n:
        print(1)
    else:
        print(fac(n)//(fac(n-r) * fac(r)))
