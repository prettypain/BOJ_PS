import sys
input = sys.stdin.readline
v = ['a', 'e', 'i', 'o', 'u']
c = [chr(i) for i in range(97, 123) if not i in v]
while(s:=input().strip())!='end':
    tar = s
    cond1, cond2, cond3 = False, True, True
    #cond1
    
    for i in v:
        if i in tar: cond1 = True

    #cond2
    count_v = 0
    count_c = 0
    for i in tar:
        if i in v:
            count_v += 1
            count_c = 0
        else:
            count_v = 0
            count_c += 1

        if count_c!=0 and count_c%3==0: cond2 = False
        if count_v!=0 and count_v%3==0: cond2 = False
    
    
    #cond3
    for i in range(len(tar)-1):
        if (not tar[i] in ['e','o']) and tar[i]==tar[i+1]:
            cond3 = False

    print(f'<{tar}> is {"acceptable" if cond1 and cond2 and cond3 else "not acceptable"}.')