import sys
input = sys.stdin.readline
def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)
    
    

for _ in range(int(input())):
    n = int(input())
    arr1 = sorted(list(map(int, input().split())))
    input()
    arr2 = list(map(int, input().split()))
    for i in arr2:
        print(binary_search(arr1, i, 0, n-1))
    
