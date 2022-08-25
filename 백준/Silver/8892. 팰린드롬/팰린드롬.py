from sys import stdin
def is_pil(target):
    l = len(target)
    a,b = target[:l//2], target[l//2+(1 if l%2!=0 else 0):][::-1]
    return a==b
input = stdin.readline
for _ in range(int(input())):
    res = 0
    lst = [input().rstrip() for i in range(int(input()))]
    arr = lst.copy()
    for i in arr:
        tmp = arr.copy()
        tmp.remove(i)
        for j in tmp:
            res = i+j if is_pil(i+j) else j+i if  is_pil(j+i) else 0
            if res: break
        if res: break
    print(res)