for _ in range(int(input())):
    n = int(input())+1
    while True:
        if str(n).count('0')==0:
            print(n)
            break
        n+=1