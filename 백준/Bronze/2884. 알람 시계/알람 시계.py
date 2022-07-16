h,m = map(int, input().split())
if m<45:
    m += 15
    if h==0:
        h=23
    else:
        h -= 1
elif m>=45:
    m -= 45
print(h,m)
