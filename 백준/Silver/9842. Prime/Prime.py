'''
시간복잡도 최대한 줄일려고 n 입력 단위별로 구하는 범위를 다르게 해서 최적화 하려고
했는데 일단 소수 10000개까지 구하게 짜고 돌렸는 완전 여유....

tmi로 104729까지 구해야 소수 10000개 딱 나온다(직접 범위 구함 ㅋㅋㅋ)
'''
def sieve(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst))
print(sieve(104729)[int(input())-1])