'''
이 문제에서 나올 수 있는 경우의 수는 총 4가지 이다.
-N이 5로 나눠질 때
-N이 5와 3의 조합으로 나눠질 때
-N이 3으로 나눠질 때
-N이 3과 5로 나눠지지 않을 때
'''
n = int(input())
if n%5==0:
    print(n//5)
else:
    s = 0 #sugar 결과 수
    while n>0:
        n-=3
        s+=1
        if n%5==0:#최소한의 3포대를 이용하는 와중에 5로 나눠질 때
            print(s+n//5)
            break
        elif n==1 or n==2:#3과 5로 나눌 수 없을 때
            print(-1)
            break
        elif n==0:#이 되는 경우는 3밖에 없다 5는 위에 if문이 있기 떄문
            print(s)
            break