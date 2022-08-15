'''
문제가 처음에는 어려워보였는데 방식을 생각해 냈더니 쉽게 느껴졌습니다.

먼저 문제를 푼 방법을 설명해 보면
예를 들어
"adaabc aababbc" 를 입력 받았을 때를 가정해 설명해 보겠습니다.
먼저 우린 a,b 값의 길이가 같을 때 각각의 인덱스 위치에 해당하는 값이 다른 정도를
최소화 해야 합니다.(이때 a의 길이는 b보다 작거나 같다
그래서 저는 부족한 a의 길이를 b의 길이와 같을 때 까지 공백으로 채우고
그 공백의 인덱스에 해당하는 b의 값을 가져와 공백에 채우는 형식으로 했습니다.
그리고 위치 이동에 대해서도 고려해야합니다.
또한 공백이 앞에 있는 경우가 답이 되는 경우일 수 있으므로 그 경우또한
추가했습니다.

결과적으로
"adaabc "
" adaabc"
총 두번 반복하는 것을 볼 수 있습니다.
(반복하는 횟수) = (b의 길이 {왜냐하면 b는 a보다 크거나 같기 떄문}) - (a의 길이) + 1(현재 위치의 경우의 수도 포함)

'''
from sys import stdin
a,b = stdin.readline().split()
lst = [] #차이 값 저장용
dif = len(b)-len(a)
for i in range(dif+1):
    t = " "*i + a + " "*(dif-i)
    res = ""
    for j in range(len(b)):
        if t[j] == " ": #문자를 채워야할 대상이라면
            res += b[j]
        else:
            res += t[j]

    #차이 계산 후 저장
    c = 0
    for j in range(len(b)):
        if res[j] != b[j]: c+=1
    lst.append(c)
print(min(lst))
