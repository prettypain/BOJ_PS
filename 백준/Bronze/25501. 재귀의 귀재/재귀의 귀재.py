def isPalindrome(string, start, end):
    c[0] += 1
    if start >= end: return 1
    elif string[start] != string[end]: return 0
    else: return isPalindrome(string, start+1, end-1)

for i in range(int(input())):
    c = [0]
    t = input()
    
    print(isPalindrome(t, 0, len(t)-1), c[0])