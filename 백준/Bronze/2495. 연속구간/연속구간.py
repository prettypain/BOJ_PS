for i in range(3):
    n = input()
    List = []
    c = 1
    before = n[0]
    for i in n[1:]:
        if i == before:
            c+=1
        else:
            List.append(c)
            c = 1
        before = i
    print(max(map(int, List+[c])))

