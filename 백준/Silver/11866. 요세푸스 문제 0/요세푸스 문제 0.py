n,k = map(int, input().split())
List = list(range(1,n+1))
arr = []
num=0
for i in range(n):
    num+= k-1
    if num >= len(List):
        num%=len(List)
    arr.append(str(List.pop(num)))
print("<", ", ".join(arr[:]),">",sep='')
