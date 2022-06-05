List = [0]*1001
s = 0
for _ in range(10):
    n = int(input())
    List[n]+=1
    s+=n
print(int(s/10))
print(List.index(max(List)))
    
