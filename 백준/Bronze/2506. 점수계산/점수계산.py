f = 1#가중치 정답을 맞추면 다음 문제에서 정답일 때 가중치 만큼 더받게 됨
n = int(input())
List = list(map(int, input().split()))
s = 0
for i in List:
    if i==1:
        s+= f
        f+=1
    else:
        f=1
print(s)
