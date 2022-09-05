lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, 100): lst.append(lst[i-1] + lst[i-5])
for i in range(int(input())):
    n = int(input())
    print(lst[n-1])
