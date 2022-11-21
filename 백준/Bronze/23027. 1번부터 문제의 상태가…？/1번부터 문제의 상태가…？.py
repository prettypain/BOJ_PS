s = input()
dic = {"A" : ["B", "C", "D", "F"], "B" : ["C", 'D', 'F'], 'C' : ['D', 'F'], "" : "A"}
for i in dic.keys():
    if i in s or i=="":
        for k in dic[i]: s = s.replace(k, i)
        s = "A"*len(s) if i=="" else s
        break
print(s)