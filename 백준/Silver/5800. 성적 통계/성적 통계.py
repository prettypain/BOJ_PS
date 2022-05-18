n = int(input())
for c in range(n):
    arr = list(map(int, input().split()))[1:]
    sa = sorted(arr)
    List = []
    for i in range(1,len(sa)):
        List.append(sa[i]-sa[i-1])
    print(f'Class {c+1}\nMax {max(arr)}, Min {min(arr)}, Largest gap {max(List)}')