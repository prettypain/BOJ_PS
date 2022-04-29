List = []
for i in range(1,10000):
    if i<10:#한자리
        List.append(i+i)
    elif i<100:#두자리
        List.append(i+i//10+i%10)
    elif i<1000:#세자리 900
        tmp = i 
        i100 = i//100 
        i%=100
        i10 = i//10
        List.append(tmp+i100+i10+i%10)
    elif i<10000:#네자리
        tmp = i
        i1000 = i//1000
        i%=1000
        i100 = i//100
        i%=100
        i10 = i//10
        List.append(tmp+i1000+i100+i10+i%10)
List = sorted(set(range(1,10000)) - set(List))
for i in List:
    print(i)
