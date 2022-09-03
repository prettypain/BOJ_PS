'''
설명 맛집(설명만 봄) : https://butter-shower.tistory.com/226
나중에 추가 설명함
'''
start, end, s, c = 0, 0, 0, 0
n,target = map(int, input().split())
lst = list(map(int, input().split()))
while end < n:
    s = sum(lst[start:end+1])
    #print(start, end, s)
    if s==target:
        c+=1
        start+=1
    elif end!=n and s<target: end += 1
    else: start+=1
print(c)