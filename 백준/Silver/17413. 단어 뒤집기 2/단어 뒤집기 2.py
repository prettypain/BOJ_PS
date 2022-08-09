'''
솔직히 문제 처음보고 "이 문제는 웰논이군요"라고 생각했는데
바로 문제의 여러 케이스한테 뚜둘겨 맞고 30분만에 해결...흑흑...

문제의 핵심은 <>안에는 그대로 나머지는 반대로이다(기준이 있음)
아래 기준이 충족되면 뒤집음
1. <인 경우
    이전까지의 것들을 모두 뒤집음
2. " "(공백)인 경우
    위와 같고 " " 값을 추가함(tmp에 추가하지 말고 마지막에 res+=tmp[::-1]+" "형식으로 추가
    tmp에다가 추가하면 공백도 뒤집힘

내가 한 방법은 그냥 <>안은 그대로 res에 추가하고 나머지는 tmp에 쌓아두다가
기준에 만족하면 그때 뒤집어서 기준에 맞게 res에 추가함
이후 출력
'''
from sys import stdin
res = ""
tmp = ""
status = False #<>부등호 범위 in out 체크용
for i in stdin.readline().rstrip():
    if i=="<":
        status = True
        if len(tmp)>0:
            res += tmp[::-1]
            tmp = ""
    elif i==">":
        status = False
        res += ">"
        continue

    if status:
        res += i
    elif i==" ":
        res += tmp[::-1]+i
        tmp = ""
    else:
        tmp += i
print(res+tmp[::-1])