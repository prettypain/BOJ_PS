for _ in range(int(input())):
    n,df,af,change = int(input()),input(),input(),[0, 0]#black, white
    for i in range(n):
        if df[i] != af[i]: change[0 if df[i]=="W" else 1] += 1
    print(f'{max(change)}')
