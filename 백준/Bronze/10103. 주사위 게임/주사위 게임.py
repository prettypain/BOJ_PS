chang = 100
sang = 100
for _ in range(int(input())):
    a,b = map(int ,input().split())
    if a > b: #창영이가 이긴 경우
        sang -= a
    elif b > a:
        chang -= b
print(f'{chang}\n{sang}')