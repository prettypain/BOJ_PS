#https://ko.wikipedia.org/wiki/%EC%9D%B4%ED%95%AD_%EA%B3%84%EC%88%98
#https://oper6210.tistory.com/76
#https://help.acmicpc.net/judge/rte/RecursionError
#이 문제는 재귀횟수를 늘린다고 해결되는게 아니라(메모리 초과...)
#그러므로 그냥 for문으로 돌려서 값을 구하면 된다.(굉장히 물리적으로)
def fac(n):
    res = 1
    for i in range(2,n+1):
        res*=i
    return res

n,k = map(int, input().split())
res = int(fac(n)/(fac(n-k)*fac(k)))
print(res)
