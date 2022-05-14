n = int(input())
for _ in range(n):
    c = 0
    length, idx = map(int, input().split())
    arr = list(map(int, input().split()))
    
    while True:
        #print(arr, idx)
        m = max(arr)
        if idx==0:
            if arr[0] == m:
                c+=1
                break
            idx = len(arr)-1
            arr.append(arr.pop(0))
             
        elif arr[0] == m:
            c+=1
            arr.pop(0)
            idx-=1
        else:
            arr.append(arr.pop(0))
            idx-=1
    print(c)
            
