def eliminater(s):
    s = list(s)
    res = []
    for i in s:
        if i==":" or (ord(i)>=48 and ord(i)<=57): res.append(i)
    return "".join(res)