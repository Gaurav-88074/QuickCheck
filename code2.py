from functools import lru_cache


@lru_cache(None)
def compute(n,k,index,target,v,array,dp):
    
    if(target==0 and n==0):
        # print(v)
        dp[n][index][target] = 1
        return 1
    if n<=0 or target<0:
        # dp[n][index][target] = 0
        return 0
    if dp[n][index][target] !=-1:
        return dp[n][index][target]
    #-----------
    res =0
    for i in range(k):
        # v.append(array[i])
        # print()
        #(i+1)
        if  n-1<0 or i<0 or target-(i+1)<0:
            continue
        if dp[n-1][i][target-(i+1)]!=-1:
            res+=dp[n-1][i][target-(i+1)]
        else:
            value=compute(n-1,k,i,target-(i+1),v,array,dp)
            dp[n-1][i][target-(i+1)] = value
            res+=value
        # v.pop()
    
    return res
n = 30
k = 30
target = 500

array= [i for i in range(1,k+1)]
dp = []
for i in range(n+1):
    dp.append([0]*(k+1))
for i in range(n+1):
    for j in range(k+1):
        dp[i][j] = [-1] * (target+1)
# print(dp)

res = compute(n,k,0,target,[],array,dp)
m = 10**9 +7
print(res%m)






