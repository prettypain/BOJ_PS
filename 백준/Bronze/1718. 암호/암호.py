#List = list(map(lambda x : ord(chr(x))-97, range(97,123)))
List =[chr(i) for i in range(97,123)]
tar = input()
key = input()
l = len(key)
res = ""
for idx, val in enumerate(tar):
    if val == " ":
        res+=" "
        continue
    res+=List[ord(val) - ord(key[idx%l])-1]
print(res)
