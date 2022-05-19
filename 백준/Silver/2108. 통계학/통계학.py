'''
최빈값 이외의 값들은 전부 쉬운수준이다.
문제의 최빈값 같은 경우 다행이 입력 정수의 범위가 -4000~4000이라 최악의 경우 8000개의 수가 모두 동일하게
입력될 수도 있는데 이와같은 경우는 별로 문제가 되지 않으므로 그대로 진행
해결방식은 단순 카운팅 방식이다.
'''
import sys
input = sys.stdin.readline
List = [] #입력받은걸 담는 통
arr1 = [0]*4002#빈도수 저장 통 양수
arr2 = [0]*4002#빈도수 저장 통 음수
marr = [] #최대 빈도수 저장 통

n = int(input())
for _ in range(n):
    tmp = int(input())
    if tmp>0: arr1[tmp]+=1
    else: arr2[abs(tmp)]+=1
    List.append(tmp)
List.sort()
m = max(arr1+arr2)
for i in range(4001):
    if arr1[i] == m: marr.append(i)
    if arr2[i] == m: marr.append(-i)
marr = sorted(marr)
for i in [round(sum(List)/n +0.00001), List[int(n/2)], marr[1] if len(marr)>1 else marr[0], max(List) - min(List)]:
    print(i)