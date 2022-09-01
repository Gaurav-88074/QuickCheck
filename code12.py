num = [0,1,2,3,4,5,6,7,8,9]

l=[]
file = open("password.txt","w")
d = []
def comb():
    if len(l)==4:
        # print(l)
        v = ("".join(map(str,l)))
        d.append(v)
        return 
    for i in range(9,-1,-1):
        l.append(i)
        comb()
        l.pop()
comb()
line = ""
for i in range(len(d)):
    
    if i%10==0:
        file.write(line+"\n")
        line = ""
    line+="  "+d[i]
