#
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**5)

def cutTheTree(data, edges):
    total = sum(data) 
    res = [float('inf')]
    tree = defaultdict(list)
    for a,b in edges:
        tree[a].append(b)
        tree[b].append(a)
    def compute(node,visited,res):
        
        visited.add(node)
        
        summ = 0
        for nextNode in tree[node]:
            if nextNode not in visited:
                value= compute(nextNode,visited,res)
                summ+=value
                res[0] = min(res[0], abs(total-2*value))
        return summ + data[node-1]
    visited = set()
    compute(1,visited,res)
    # print(len(Visited))
    return res[0]
        
    # Write your code here

if __name__ == '__main__':
    file = open("input.txt", 'r')
    txt = file.readlines()
    i = 0
    # for i in  data:
    #     print(i,4)
    # print(txt)

    n = int(txt[i].replace('\n',""))
    i+=1
    data = list(map(int, txt[i].replace('\n',"").rstrip().split()))
    i+=1
    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, txt[i].replace('\n',"").split())))
        i+=1
    i+=1
    result = cutTheTree(data, edges)
    # print(result)
    output = open("output.txt","w")
    output.write(str(result) + '\n')

    output.close()
