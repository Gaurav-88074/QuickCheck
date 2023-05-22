"""
    1
   32
  654
10987
"""
def traverse(value,currSize,rowSize,spaceSize):
    if currSize==rowSize:
        print(spaceSize * " ",end="")
        return value
    lastValue = traverse(value+1,currSize+1,rowSize,spaceSize)
    print(value,end="")
    return lastValue

space =" "
i = 1
rowSize = 1
spaceSize = 4
while (i<10):
    i = traverse(i,0,rowSize,spaceSize)
    spaceSize-=1
    print()
    rowSize+=1


# [1,2,3,4]
# 5
# 4
# 3
# 2
# 1