def f(arr):
    c = 0
    c1 = 0
    for i in range(8):
        tmp = arr[i]
        if i==0:original = tmp[0]
        if i%2==0:
            start = original
            for k in range(8):
                if tmp[k]!=start:
                    c+=1
                else:
                    c1+=1
                start = "W" if start=="B" else "B"
        else:
            start = "W" if original=="B" else "B"
            for k in range(8):
                if tmp[k]!=start:
                    c+=1
                else:
                    c1+=1
                start = "W" if start=="B" else "B"
    return min(c,c1)
n,m = map(int, input().split())
List = [list(input()) for i in range(n)]
List2 = []
for i in range(n-7):
    tar = List[i:8+i]
    for j in range(m-7):
        temp_List = [0,0,0,0,0,0,0,0]
        for k in range(8):
            temp_List[k] = tar[k][j:8+j]
        List2.append(f(temp_List))
print(min(List2))