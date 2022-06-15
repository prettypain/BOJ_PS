NOTATION = '0123456789ABCDEF'
def numeral_system(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

while True:
    tmp = input()
    if tmp == "0":break
    t, a, b = tmp.split()
    t = int(t)
    print(numeral_system((int(a,t)%int(b,t)), t))