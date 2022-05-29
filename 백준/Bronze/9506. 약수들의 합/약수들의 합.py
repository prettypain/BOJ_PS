while True:
    n = int(input())
    if n == -1: break

    List = [i for i in range(1,n) if n%i==0]
    s = sum(List)
    if s == n:
        print(f'{n} =',' + '.join(map(str, List)))
    else:
        print(f'{n} is NOT perfect.')
