

def distance(p1,p2):
    res  = ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5 
    return res

def compute(array,k):
    res=0;
    for i in range(len(array)):
        
        for j in range(len(array)):
            if i!=j and array[i]!=None and array[j]!=None and distance(array[i],array[j])<=k :
                res+=1
                array[j] = None
        
    return res
a,b = list(map(int,input().split(" ")))
point = []            
for i in range(a):
    x,y = list(map(int,input().split(" ")))
    point.append([x,y])
print(compute(point,b))
"""
4 1
1 2
2 1
1 1 
2 2
"""
"""
5 1
1 1
1 2
1 3
1 4
1 5
"""