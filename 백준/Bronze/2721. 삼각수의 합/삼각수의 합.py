'''
자세히 : https://bmy1320.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Bronze3-%EB%AC%B8%EC%A0%9C-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2721-%EB%B0%B1%EC%A4%80-2721-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2721
ex)
n = 3 입력되었으면
1*T(1+1) = T(2) = 1+2 =3
2*T(2+1) = 2 * T(3) = 2 * (1+2+3) = 12
3*T(3+1) = 3 * T(4) = 3 * (1+2+3+4) =30
'''

for _ in range(int(input())):
    n = int(input())
    s = 0
    for i in range(1,n+1):
        s += i*sum(range(1,i+2))
    print(s)