y,k = 0,0
for i in range(int(input())):
    for j in range(9):
        a,b = map(int, input().split())
        y+=a
        k+=b
    print('Draw' if y==k else ('Yonsei' if y>k else 'Korea'))