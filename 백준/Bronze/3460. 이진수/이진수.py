for _ in range(int(input())):
    for idx, val in enumerate(bin(int(input()))[2:][::-1]):
        if int(val)==1:
            print(idx,end=" ")
