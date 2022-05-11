import sys, math
input = sys.stdin.readline
List = sorted([int(input()) for i in range(9)])
for a in List:
    tmp = List.copy()
    tmp.remove(a)
    for b in tmp:
        tmp1 = tmp.copy()
        tmp1.remove(b)
        for c in tmp1:
            tmp2 = tmp1.copy()
            tmp2.remove(c)
            for d in tmp2:
                tmp3 = tmp2.copy()
                tmp3.remove(d)
                for e in tmp3:
                    tmp4 = tmp1.copy()
                    tmp4.remove(c)
                    for f in tmp4:
                        tmp5 = tmp4.copy()
                        tmp5.remove(d)
                        for g in tmp5:
                            if a+b+c+d+e+f+g==100:
                                for k in [a,b,c,d,e,f,g]:
                                    print(k)
                                sys.exit()