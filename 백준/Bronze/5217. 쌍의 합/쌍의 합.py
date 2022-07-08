n = int(input())
for _ in range(n):
    t = int(input())
    List = []
    for i in range(1,t+1):
        for j in range(1,t+1):
            if i<j and i+j==t:
                List.append([i,j])
    if len(List)==0:
        print(f"Pairs for {t}: ")
    elif len(List)==1:
        List=List[0]
        print(f"Pairs for {t}: {' '.join(map(str,List))}")
    else:
        print(f"Pairs for {t}:",end=" ")
        for i in List[:len(List)-1]:
            print(' '.join(map(str, i)),end=", ")
        print(' '.join(map(str,List[-1])))