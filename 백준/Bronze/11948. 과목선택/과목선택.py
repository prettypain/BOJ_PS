a = int(input())#물
b = int(input())#화
c = int(input())#생
d = int(input())#지
e = int(input())#역
f = int(input())#지뤼
print(sum(sorted([a,b,c,d], reverse=True)[:3]) +max(e,f))
