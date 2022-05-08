import sys
def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    return binary_search(arr, target, mid+1, end)

input = sys.stdin.readline
input()
List = sorted(map(int, input().split()))
input()
for i in list(map(int, input().split())):
    print(binary_search(List, i, 0, len(List)-1))