s = ""
bf = ""
for i in input():
    if bf!=i:
        s+=i
        bf = i
print(s)