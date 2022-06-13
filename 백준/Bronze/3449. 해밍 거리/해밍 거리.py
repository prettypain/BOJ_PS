for _ in range(int(input())):
    a=input()
    b=input()
    c = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            c+=1
    print("Hamming distance is "+str(c)+".")