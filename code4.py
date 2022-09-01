
# 3186
def check(a,b,start):
    for i in range(len(a)):
        if a[i]!=b[start+i]:
            return False
    return True
def matchReplacement(s, sub,mappings):
        d = dict()
        for l in mappings:
            if l[0] in d:
                d[ l[0]].add(l[1])
            else:
                d[ l[0] ] = set(list(l[ 1 ]))
        # print(d)
        #--set---
        s = list(s)
        
        # start = 0
        # end = len(sub)-1
        
        substr = list(sub)
        for i in range(len(s) - len(sub)+1):
            # print(substr,s[i : i+len(sub)])
            start = i
            end = start + len(sub)-1
            index = 0
            while(start<=end):
                # print(start,end)
                if(substr[index] != s[start]):
                    if substr[index] in d:
                        if s[start] in d[substr[index]]:
                            substr[index] =  s[start]
                        # if d[substr[index]] == s[start]:
                           
                index+=1
                start+=1
            print(substr,s[i : i+len(sub)])
            # print("----------------")
            if(check( substr,s,i)):
            
                return True;
            substr = list(sub)
        return False

s = "fool3e7bar"
sub = "leet"
mappings = [["e","3"],["t","7"],["t","8"]]
res = matchReplacement(s, sub,mappings)
print(res)


