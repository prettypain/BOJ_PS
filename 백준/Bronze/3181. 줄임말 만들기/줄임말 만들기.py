lst = input().split()
t = ""
arr = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
for i in range(len(lst)):
    if i!=0 and lst[i] in arr: continue
    t+= lst[i][0].upper()
print(t)