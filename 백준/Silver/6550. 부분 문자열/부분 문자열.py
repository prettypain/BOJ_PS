while True:
    try:
        s,t = input().split()
        c = 0
        j = 0
        for i in range(len(t)):
            if c==len(s): break
            if t[i] == s[j]:
                c+=1
                j+=1
                continue
        print("Yes" if c==len(s) else "No")
    except:
        break