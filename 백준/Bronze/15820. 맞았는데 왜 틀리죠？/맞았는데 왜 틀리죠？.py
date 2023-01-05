sample = True
sys = True
s1, s2 = map(int, input().split())
for _ in range(s1):
    a,b = map(int, input().split())
    if a!=b: sample = False
for _ in range(s2):
    a,b = map(int, input().split())
    if a!=b: sys = False
print("Accepted" if sample and sys else  "Why Wrong!!!" if sample else "Wrong Answer")