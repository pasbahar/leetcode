def partition(s):
    def isPalindrome(s):
        return s == s[::-1]
    def palinPart(s,ind,ans,res):
        if ind == len(s):
            res.append(ans[:])    
            return
        for i in range(ind,len(s)):
            if isPalindrome(s[ind:i+1]):
                temp = s[ind:i+1]
                ans.append(temp)
                palinPart(s,i+1,ans,res)
                ans.pop()
    res = []
    palinPart(s,0,[],res)
    return res
print(partition('aab'))
        