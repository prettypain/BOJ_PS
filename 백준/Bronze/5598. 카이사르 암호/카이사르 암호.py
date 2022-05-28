List = [chr(i) for i in range(65,91)]
w = ""
for i in input():
    w+=List[ord(i)-68]
print(w)
