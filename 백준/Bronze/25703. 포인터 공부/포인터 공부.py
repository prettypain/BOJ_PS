n = int(input())
print("int a;")
print("int *ptr = &a;")
for i in range(n-1): print(f"int {'*'*(i+2)}ptr{i+2} = &ptr{'' if i==0 else i+1};")