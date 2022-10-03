from typing import Counter
n = int(input())
arr = []
res = 0
for i in range(n):
    s = input().rstrip()
    arr.append(s)

def compute(s):
    for i in range(0,len(s)-1):
        if s[i]=='b' and s[i+1]=='a':
            return False
    return True
    
for s in arr:
    c  = Counter(s)
    # print(c)
    if len(c)>2:
        continue
    if 'a' in c and 'b' in c and compute(s)==True:
        res+=1
print(res)