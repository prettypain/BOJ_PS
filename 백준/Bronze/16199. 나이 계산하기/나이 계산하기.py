# year mon day
p = list(map(int, input().split()))
stan = list(map(int, input().split()))

print(stan[0]-p[0]-1 + (1 if stan[1]>p[1] or (stan[1]==p[1] and stan[2]>=p[2])else 0))
print(stan[0]-p[0] + 1)
print(stan[0]-p[0])