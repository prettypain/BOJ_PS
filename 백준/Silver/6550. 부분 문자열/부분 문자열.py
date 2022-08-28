'''
s와 t가 입력으로 주어졌을 때
t를 하나씩 반복하면서 s[j]와 같으면 j를 1씩 증가시켜준다.
최종적으로 j와 len(s)가 같다면(마지막 s[-1]이 맞으면 j도 최종적으로 len(s)와 같아짐)정답
'''
from sys import stdin
while True:
    try:
        s,t = stdin.readline().rstrip().split()
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j+=1
                if j==len(s): break
                continue
        print("Yes" if j==len(s) else "No")
    except:
        break
