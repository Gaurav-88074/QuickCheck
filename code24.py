res = 0
s = [2,3,5,7,11,13,17,19]
for i in range(10,100):
    v = str(i)
    
    f = 1
    for j in range(0,len(v)-1):
        if (int(v[j])+int(v[j+1])) in s:
            f=0
            break
    if f==1:
        print(v)
        res+=1
print(res)
