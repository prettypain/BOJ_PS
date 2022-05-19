import sys
input = sys.stdin.readline
List = [] #입력받은걸 담는 통
arr1 = [0]*4002#빈도수 저장 통 양수
arr2 = [0]*4002#빈도수 저장 통 음수

n = int(input())
for _ in range(n):
    tmp = int(input())
    if tmp>0:
        arr1[tmp]+=1
    else:
        arr2[abs(tmp)]+=1
    List.append(tmp)
List.sort()
m = max(arr1+arr2)
marr = []
for i in range(4001):
    if arr1[i] == m:
        marr.append(i)
    if arr2[i] == m:
        marr.append(-i)
marr = sorted(marr)


avg = round(sum(List)/n +0.00001)#산술 평균 
mid = List[int(n/2)]#중앙값
cbin = marr[1] if len(marr)>1 else marr[0]#최빈값
rang = max(List) - min(List)
for i in [avg,mid,cbin,rang]:
    print(i)
