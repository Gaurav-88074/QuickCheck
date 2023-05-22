import random
def generate(size):
    res = []
    for i in range(size):
        res.append(random.randint(1,10**8))
    return res
# v = generate(10)
# print(v)

def generateValue(a,b):
    
    res = random.randint(a,b)
    return res
for i in range(100):
    print(generateValue(1,2**31 -1))