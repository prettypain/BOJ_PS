'''
s와 t가 입력으로 주어졌을 때
t를 하나씩 반복하면서 s[j]와 같으면 c와 j를 각각1씩 증가해준다.
최종적으로 c와 len(s)가 같다면(마지막 s[-1]이 맞으면 c도 최종적으로 len(s)와 같아짐)
정답
'''
from sys import stdin
input = stdin.readline
while True:
    try:
        s,t = input().rstrip().split()
        c = 0
        j = 0
        for i in range(len(t)):
            if c==len(s): break
            if t[i] == s[j]:
                c+=1
                j+=1
                continue
        print("Yes" if c==len(s) else "No")
    except:
        break