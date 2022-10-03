s = input().rstrip()
target = input().rstrip()
d = [0]*26
for i in s:
    v = ord(i)-97
    d[v]+=1
res = 0
temp = []
for k in range(100):
    for i in target : 
        v = ord(i)-97
        if d[v]!=0:
            temp.append(i)
            d[v]-=1
s = "".join(temp)

print(s.count(target))