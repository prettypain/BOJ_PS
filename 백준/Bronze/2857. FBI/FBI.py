pb = True
for i in range(5):
    t = input()
    if t.count("FBI"):
        print(i+1,end=" ")
        pb = 0
if pb:print("HE GOT AWAY!")
