k, l = map(int, input().split())
pb = False
for i in range(2, l):
    if k%i==0:
        pb = True
        break
print(f"BAD {i}" if pb else "GOOD")