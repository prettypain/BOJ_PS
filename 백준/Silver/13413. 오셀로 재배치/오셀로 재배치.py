for _ in range(int(input())):
    n = int(input())
    df = input()
    af = input()
    change = [0, 0] #black, white
    for i in range(n):
        if df[i] != af[i]: change[0 if df[i]=="W" else 1] += 1

    if not (change[0] and  change[1]): #[0, >0] or [>0, 0]
        print(sum(change))
    else:
        print(max(change))