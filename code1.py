def generate(n,b,open,close,i):
    if i == 2*n :
        print(b)
        return
    if open<n:
        generate(n, b+"(", open+1, close,i+1)
    if open>close:
        generate(n, b+")", open, close+1,i+1)
generate(3,"",0,0,0)