mod = 10**8 + 7
n=int(input())
res = 1
for i in range(1,n+1):
    res*=i
    res%=mod
print(res)