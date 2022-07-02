for i in range(3):
    a,b,c, h,m,s = map(int, input().split())
    h = h-a
    m = m-b
    s = s-c
    if s<0:
        m-=1
        s+=60
    if m<0:
        h-=1
        m+=60
    print(h,m,s)