a = sum([int(input())*i for i in range(3,0,-1)])
b = sum([int(input())*i for i in range(3,0,-1)])
print("A" if a>b else "B" if b>a else "T")
