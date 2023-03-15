n = int(input())
score = [int(input()) for _ in range(n)]
step = [0]*n

step[0] = score[0]
if n>1: step[1] = score[0] + score[1]
if n>2: step[2] = score[2] + max(score[1], score[0])

for i in range(3, n):
    #step[i] = 현재계단 점수
    #+ max(2칸전에 2연속 밟은점수, 3칸전점수(3칸전+4칸전:2연) + 1칸전 점수)
    step[i] = score[i] + max(step[i-2], step[i-3]+score[i-1])
print(step[-1])