n,m=map(int,input().split())
print("NEWBIE!" if m in [1,2] else ("OLDBIE!" if n>=m else "TLE!"))