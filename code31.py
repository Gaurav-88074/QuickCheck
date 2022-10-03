from functools import lru_cache


def countVowelStrings(n: int) -> int:
        
        vowels = ["a","e","i","o","u"]
        arr = []
        
        @lru_cache(None)
        def compute(n,index):
            
            if n==0 : return 1
            
            return sum([ compute(n-1,i) for i in range(index,5)])
            
        return sum([compute(n-1,index) for index in range(5)])

arr = []
for i in range(1,51):
    arr.append(countVowelStrings(i))
print(arr)