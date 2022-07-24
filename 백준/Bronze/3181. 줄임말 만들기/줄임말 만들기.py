'''
간단하다
그냥 0번째가 아닌데 차단목록에 있는 것들만 처내고 나머지들의 0번째 문자를 대문자로
바꾼다음 저장해 출력하면 끝~
'''
from sys import stdin
t = ""
arr = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
lst = stdin.readline().split()
for i in range(len(lst)):
    if i!=0 and lst[i] in arr: continue
    t+= lst[i][0].upper()
print(t)
