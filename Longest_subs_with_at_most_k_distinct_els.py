def util(s,k,l,r,maxlen):
    d={}
    mid=(l+r)//2
    for i in s:
        d[i]=True
    if len(d)>k:
        util(s,k,l,mid,maxlen)
        util(s,k,mid,r,maxlen)
    elif len(d)==k:
        maxlen[0]=r-l
        return
    else:
        return

def findsub(s,k):
    maxlen=[0]
    return util(s,k,0,len(s),maxlen)