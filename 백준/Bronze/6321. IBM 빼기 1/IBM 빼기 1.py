n = int(input())
lst = [chr(i) for  i in range(65,91)]+["A"]
for c in range(n):print(f'String #{c+1}\n'+''.join([lst[ord(i)-64] for i in input()]),end="\n\n")