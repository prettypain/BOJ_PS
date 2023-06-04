while True:
    n = int(input())
    if n==0: break
    if 1000000<n<=5000000:
        print(int(n*0.9))
    elif 5000000<=n:
        print(int(n*0.8))
    else:
        print(n)
