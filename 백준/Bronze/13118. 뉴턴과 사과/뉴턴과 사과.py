lst = list(map(int, input().split()))
tar = int(input().split()[0])
print(lst.index(tar)+1 if tar in lst else 0)
