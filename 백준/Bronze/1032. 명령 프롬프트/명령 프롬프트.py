n = int(input())
List = [input() for i in range(n)]
for idx, val in enumerate(List[0]):
    s = False
    for i in range(1,len(List)):
        if List[i][idx] != val:
            s = True
            break
    if s:
        print("?",end="")
    else:
        print(val,end="")
