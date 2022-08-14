'''
A, B, BA, BAB, BABBA
"B는 BA로 바뀌고, A는 B로 바뀐다"
A -> B -> BA -> BB -> BAB -> BAABA -> BABBA

A->B로 변할 때는 B->BA로 변한 것들을 제외하고 기존에 있던 것들을
바꾼다(중요함)

그럼 갯수의 변화는
AC,BC = BC, AC+BC라는 식이 완성 된다.
이 식은 피보나치 수를 구할 때 사용되기도 한다.
또한 답이 피보나치 수다...

번튼을 누른 횟수 : [현재 A의 개수), (현재 B의 개수)]
라고 할 때

0 : [1, 0] A->B
1 : [0, 1] B->BA
2 : [1, 1] B->BA, A->B
3 : [1, 2] B->BA, A->B
4 : [2, 3] B->BA, A->B
5 : [3, 5] B->BA, A->B
6 : [5, 8] B->BA, A->B
7 : [8, 13] B->BA, A->B
8 : [13, 21] B->BA, A->B
9 : [21, 34] B->BA, A->B
10 : [34, 55] B->BA, A->B
규칙을 보면 피보나치 수가 생각이 난다.
'''
import sys
def fibo(n):
    memo = [0, 1]
    for i in range(n-1):
        memo.append(memo.pop(0)+memo[0])
    return memo
print(" ".join(map(str, fibo(int(sys.stdin.readline())))))