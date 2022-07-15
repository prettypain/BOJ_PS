'''
문제를 이해했다는 가정하에 진행

먼저 중요한 포인트는 문자를 선택할 때 입력된 것들과 중복이 많아야 한다
이때 입력된 것이 중복 즉
TA
TC
AC
AT
일 경우 T와 A의 개수가 같다 즉 어떤 것을 선택해도 HD(Hamming Distance)는 같은데
문제에서는 '사전 순'으로 먼저인 것을 선택하고 했다.
즉 T(84) 대신 A(65)를 선택해야 한다(여기서 아스키코드가 먼저인 것을 고르면 된다)
하지만 나는 문자와 카운팅의 인덱스를 미리 사전 순으로 하고
index(val) 메서드(오브젝트에서 가장 앞에있는 val의 인덱스 값을 리턴함)를 이용해서 풀었다.
그외에 자잘한 부분은 따로 주석을 달았음
'''
import sys
input = sys.stdin.readline

word = ['A', 'C', 'G', 'T'] #사전순으로 정렬됨
n,m = map(int, input().split())
lst = [input().rstrip() for _ in range(n)] #list comprehension방법으로 입력받음
res = "" #결과 문자열을 저정할 변
c = 0 #각 인덱스별로 다른 단어의 개수를 저장할 변수
for i in range(m): 
    tar = ''.join(map(lambda x : x[i],lst))#모든 단어의 i번째값을 가져와 하나의 문자열로 만듬
    count = [tar.count("A"),tar.count("C"),tar.count("G"),tar.count("T")]#위에서 만든 문자열를 사전순서대로 카운팅함(반복분을 사용하면 시간을 좀 먹어서 하드코딩함) 또는 아래 주석을 사용
    #count=[0]*4
    #for k in range(4): count[k] = tar.count(word[k])

    idx = count.index(max(count))#가장 많이 나온 단어의 개수의 인덱스를 저장
    res += word[idx] #그 인덱스에 해당하는 사전순서대로 정렬된 단어에서 가져옴
    count[idx] = 0 #그리고 해당 인덱스에 해당하는 값은 카운팅할 필요가 없으므로 0로 처리
    c += sum(count) #해당 인덱스 외에 모든 값을 다 더해 카운팅.
print(f'{res}\n{c}')
