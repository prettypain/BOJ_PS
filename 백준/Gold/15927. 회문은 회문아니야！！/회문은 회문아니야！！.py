s = input()
if len(s)==1 or len(s)==s.count(s[0]):
    print(-1)
elif s!=s[::-1]:
    print(len(s))
else:
    print(len(s)-1)