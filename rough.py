from collections import defaultdict, deque,ChainMap
from functools import cmp_to_key
from typing import List, Tuple, Optional
# from sortedcollections import OrderedSet
from collections import defaultdict, Counter
from sortedcontainers import SortedList, SortedDict,SortedSet
from itertools import accumulate
q = deque()
d = defaultdict(int,Counter([1,2,3]))
d = defaultdict(int)
l = SortedList(key = lambda x : x[0])
def compute(i,arr,size):
            if i>=len(arr):
                print(arr)
                return 
            for x in range(i,size):
                arr.append(x)
                compute(i+x,arr,size)
                arr.pop()
compute(1,[],4)
#2
# import math
# def isPrime(n):
#     if n==1:
#         return False
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0:
#             return False
#     return True
# res = []
# for i in range(1,10**6):
#     if isPrime(i):
#         res.append(i)
# print(res)
# print(26*6)
# d = defaultdict()
# l = SortedSet([9,7,5,1,2])
# print(l)
# # c = SortedList.bisect_left(l,5)
# c=l.bisect_left(4)
# print("index=",c)
