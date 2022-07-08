a,b,c = map(int, input().split())
aa,bb,cc,i = 0,0,0,1
#15 28 19
if a==b==c==1:
    print(1)
else:
    while 1:
        aa+=1
        bb+=1
        cc+=1
        i+=1
        if aa%15+1==a and bb%28+1==b and cc%19+1==c:
            print(i)
            break