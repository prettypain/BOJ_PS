while 1:
    t = input()
    if t[0] == "#": break
    tar, word = t[0],t[2:]
    print(tar,word.lower().count(tar))
