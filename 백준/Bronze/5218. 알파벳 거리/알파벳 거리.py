for i in range(int(input())):
    a,b = input().split()
    print("Distances: ",end="")
    for i, j in zip(a,b):
        x=ord(i)-64
        y=ord(j)-64
        print(y-x if y>=x else y+26-x,end=" ")
    print()