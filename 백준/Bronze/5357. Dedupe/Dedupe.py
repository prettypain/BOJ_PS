for _ in range(int(input())):
    s = ""
    bef = ""
    for i in input():
        if i!=bef:
            s+=i
            bef = i
    print(s)