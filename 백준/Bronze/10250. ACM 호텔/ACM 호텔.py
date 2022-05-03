n=int(input())
for _ in range(n):
    h,w,c=map(int,input().split())
    if c%h==0:print(f'{h}{(c//h):02d}')
    else:print(f'{c%h}{(c//h)+1:02d}')