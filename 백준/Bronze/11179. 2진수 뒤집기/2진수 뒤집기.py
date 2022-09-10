def notation_int_to_a(n=0, a=2): #10진수 n을 a진법으로 변환, a>=2
    if n<2: return str(n)
    elif n==2 and a==2: return '10'
    lst = list(range(a))[::-1]
    last_place = 0
    while n>a**last_place:
        last_place+=1
    res = ""
    for k in range(last_place-1, -1, -1):
        for i in lst:
            if i==0: res += '0'
            elif n >= i*(a**k):
                res += str(i)
                n%= (i*(a**k))
                break
    return res
def bin_to_int(n):
    res = 0
    pointer = len(n)
    for i in range(len(n)):
        pointer-=1
        if n[i] == '0': continue
        res += 2**pointer
    return res

n = int(input())
print(bin_to_int(notation_int_to_a(n)[::-1]))