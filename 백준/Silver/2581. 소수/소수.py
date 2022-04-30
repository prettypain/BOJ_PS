def pri(tar):
    if tar==1:return False
    #소수는 1과 자기자신이 약수이다.
    #즉 2부터 자기자신-1까지의 수중에서 자기 자신을 나눌 수 있는
    #수가 있다면 그건 소수가 아니게 된다.
    for num in range(2,tar):
        if tar%num==0:
            return False
    return True

List = []
for i in range(int(input()),int(input())+1):
    if pri(i):#소수인 경우에만 리스트에 저장.
        List.append(i)


if len(List)==0:
    print(-1)
else:
    print(f"{sum(List)}\n{min(List)}")
