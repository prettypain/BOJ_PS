dic = {
    "c=" : 0,
    "c-" : 0,
    "dz=" : 0,
    "d-" : 0,
    "lj" : 0,
    "nj" : 0,
    "s=" : 0,
    "z=" : 0
}

word = input()
c = 0
for i in dic.keys():
    wc = word.count(i)
    if wc>=1:
        c += word.count(i)
        word = word.replace(i," ")

print(c+len(word.replace(" ","")))
