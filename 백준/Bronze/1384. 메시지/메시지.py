group = 0
while(n:=int(input()))!=0:
    lst = [input().split() for i in range(n)]
    name = [i[0] for i in lst]
    print(f'Group {group+1}')
    pc = 0 #print count 
    for i in lst:
        letter = i[1:]
        c = letter.count("N")
        for j in range(c):
            who = name[name.index(i[0]) - letter.index("N") - 1]
            print(f'{who} was nasty about {i[0]}')
            letter[letter.index("N")] = ""
        pc += c
    if pc==0:
        print("Nobody was nasty")
    group += 1
    print()