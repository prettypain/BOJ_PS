#(n! / m!) / (n-m)!
n, m = map(int, input().split())
fn = 2*n
fm = 2*m
fnm = 2*(n-m)
for i in range(3, n):
    fn*=i
for i in range(3, m):
    fm*=i
for i in range(3, (n-m)):
    fnm*=i
print((fn//fm)//fnm)
