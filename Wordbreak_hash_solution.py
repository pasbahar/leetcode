def wordbreak(s, worddict):
    wd,lengths=set(),set()
    for i in worddict:
        wd.add(i)
        lengths.add(int(len(i)))
    valid_word=[False]*len(s)
    for i in lengths:
        valid_word[i]=True
    for i in range(len(s)): 
        if valid_word[i]:
            for j in lengths:
                subarr=s[i:j] #python doesn't like when you assign end from set
                if i+j<len(s) and subarr in wd:
                    valid_word[i-1+j]=True
                if i+j==len(s)-1 and valid_word[i+j]:
                    return True
    return False

print(wordbreak("leetcode", ["leet", "code"]))