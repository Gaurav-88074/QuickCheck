s = "999+999"
s =list(s)
print(s)
index = s.index("+")
def comb(p1,p2,n,s):
    if p1==-1 or p2==n+1:
        return
    nw = [*s]
    nw.insert(p1,"(")
    nw.insert(p2+1,")")
    print("".join(nw))
    # comb(p1-1,p2+1,n,s)
    comb(p1,p2+1,n,s)
    comb(p1-1,p2,n,s)
comb(index-1,index+2,len(s),s)


    
