array=[]
for i in range(1,11): 
    array.append(i)
print(array)
array.sort(key = lambda x: x&1)
print(array)