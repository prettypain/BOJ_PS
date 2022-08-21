'''
나는 딕셔너리를 사용해서 풀었다.
key값은 성적, value값은 [지역번호, 개인번호]로 했다.
key값은 유니크하다 성적이 key값으로 가능한 이유는 문제에서 " 단, 동점자는 없다고 가정한다."
라고 했기 때문이다.
그리고 모든 key값들을 내림차순으로 정렬하고(사실 정렬후 뒤집기 ㅋ) 그 순서대로

정답속에 같은지역 사람의 수를 카운트해서 그 수가 2보다 작아면 추가하고
아니면 다음걸로 넘어간다.(continue)
이후 정답의 길이가 3이라면 break

를 반복하고 res를 출력했다.
'''
from sys import stdin
input = stdin.readline
n = int(input())
dic = {}
for i in range(n):
    coutry, num, score = map(int, input().split())
    dic[score] = [coutry, num]

res = []
for i in sorted(dic.keys(), reverse=1):
    t = dic[i]
    c = 0
    for j in res:
        if j[0] == t[0]: c+= 1
    if c<2: res.append(t)
    else:continue
    if len(res)==3:break
for i in res:print(*i)