import sys
input = sys.stdin.readline

word = ['A', 'C', 'G', 'T']
n,m = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]
res = ""
c = 0
for i in range(m):
    tar = ''.join(map(lambda x : x[i],lst))
    count = [tar.count("A"),tar.count("C"),tar.count("G"),tar.count("T")]
    #count=[0]*4
    #for k in range(4): count[k] = tar.count(word[k])
    idx = count.index(max(count))
    res += word[idx]
    count[idx] = 0
    c += sum(count)
print(f'{res}\n{c}')