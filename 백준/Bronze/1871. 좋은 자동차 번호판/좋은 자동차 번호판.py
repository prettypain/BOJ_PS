for _ in range(int(input())):
    en, num = input().split("-")
    num = int(num)
    t = sum([((ord(en[i])-65)*(26**(len(en)-1-i))) for i in range(len(en))])
    print("nice" if abs(t-num)<= 100 else "not nice")