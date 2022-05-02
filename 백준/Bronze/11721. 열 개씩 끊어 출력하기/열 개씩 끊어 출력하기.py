words = input()
for i in range(len(words)):
    print(words[i],end=("\n" if (i+1)%10==0 else ""))
