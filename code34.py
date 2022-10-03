file = open('unoffical.txt','r', encoding="utf-8")
data = file.read().split("\n")
v = data
from collections import defaultdict
d = defaultdict(int)
for i in v:
    if "M - " not in i:
        continue
    text=  i.split("M - ")[1]
    if ":" not in text:
        continue
    index = text.index(":")
    text = text[:index]
    #-------------------
    d[text.lower()]+=1
    #-------------------
    # print(text)
    # text = text[:index]
    # if(len(text)<2):continue
    # print(text)
    # message = text.split(" ")
    # for word in message:
    #     d[word.lower()]+=1
arr = []
for w in d:
    arr.append([w,d[w]])
arr.sort(key = lambda x : x[1],reverse=True)
# print(arr[:50])
# print(len(d))
filew = open("unofficialstats.txt",'w',encoding="utf-8")
for word,c in arr:
    filew.write(str(word)+"  -->  "+str(c)+"\n")
filew.close()

