'''
대충 귀납적으로 가능한지 대조했는데 쌉가능
P(10) = P(9) + P(5)
P(9) = P(8) + P(4)
P(8) = P(7) + P(3)
즉
P(N) = P(N-1) + P(N-5)
가 성립되는것을 볼 수 있음
음수로 확장도 가능해 보임
'''
lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, 100): lst.append(lst[i-1] + lst[i-5])
for i in range(int(input())):
    n = int(input())
    print(lst[n-1])
