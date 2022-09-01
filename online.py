n,t= map(int,input().rstrip().split(" "))
arr= list(map(int,input().rstrip().split(" ")))
d = {}
for i in range(len(arr)):
    d[arr[i]]=i+1
for i in arr:
    if t-i in d and d[i]!=d[t-i] :
        print(d[i],d[t-i])
        break
print("IMPOSSIBLE")