f=lambda:sum([i*int(j)for i,j in zip([3600,60,1],input().split(":"))])
s1,s2=f(),f();print(s2+86400-s1 if s1>s2 else s2-s1)