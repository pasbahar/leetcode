
def util(s,ind,wordict,visits):
    if ind==len(s): return True

    if not visits[ind]:
        visits[ind]=False
        curr=s[ind:]
        for i in wordict:
            if curr[:len(i)]==i and util(s,ind+len(i),wordict,visits):
                visits[ind]=True
                break
    return visits[ind]
    



def wordbreak(s,wordict):
    visits=[None]*len(s)
    return util(s,0,wordict,visits)

s = "applepenapple"
wordDict = ["apple", "pen"]
print(wordbreak(s,wordDict))