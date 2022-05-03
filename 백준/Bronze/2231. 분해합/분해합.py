n = int(input())
List = [] #n의 생성자에 해당자를 넣어놓을 곳
for i in range(1,n):
    si = str(i)
    tmp = i
    for k in si:
        tmp += int(k)
    if tmp == n:
        List.append(i)
print(min(List) if len(List)!=0 else 0)
