from collections import Counter
from typing import Counter

s = input()
res = []
pre ="#"
c = 0
for i in s:
    if i==pre:
        c+=1
    else:
        v = min(2,c)
        res.append(v*pre)
        c=1
    pre = i
v = min(2,c)
res.append(v*pre)
ans = "".join(res[1:])
print(ans)

def findTheWinner(self, n: int, k: int) -> int:
        ls = [i for i in range(1,n+1)]
        s=0
        while len(ls) != 1:
            rem = (s + k-1) % len(ls)
            ls.pop(rem)
            s = rem
        
        return ls[0]