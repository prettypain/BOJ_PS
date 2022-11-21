def f(target):
    #return value is ‘Perfect’, ‘Deficient' or ‘Abundant’.
    arr = [i for i in range(1, target) if target%i==0]
    return sum(arr)
n = int(input())
lst = list(map(int, input().split()))
for i in lst:
    res = f(i)
    print("Perfect" if i==res else "Deficient" if i > res else "Abundant")