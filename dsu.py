def find(node,parent):
    if parent[node]==node:
        return node
    parent[node]= find(parent[node],parent)
    return parent[node]
def union(x,y,rank,parent):
    x_rep = find(x)
    y_rep = find(y)
    if x_rep==y_rep:
        return
    else:
        if rank[x_rep]<rank[y_rep]:
            parent[x_rep]=y_rep
        elif rank[x_rep]>rank[y_rep]:
            parent[y_rep]=x_rep
        else:
            parent[x_rep]=y_rep
            rank[y_rep]+=1
