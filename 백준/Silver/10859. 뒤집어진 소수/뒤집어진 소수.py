def clock_drop(target):
    target = str(target)
    res = ""
    for i in target:
        if i == "6": res+="9"
        elif i=="9": res += "6"
        elif i in ['3', '4', '7']:
            return False #문제 있는 숫자는 거짓으로 리턴
        else: res += i
    return res[::-1]

def is_prime(n): #소수 판정
    if n==1 or (n!=2 and n%2==0): return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True

t = int(input())
rev = clock_drop(t)
print("yes" if rev and is_prime(t) and is_prime(int(rev)) else "no")