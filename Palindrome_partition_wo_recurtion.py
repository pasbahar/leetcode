def partition(s):
    def isPalindrome(s):
        return s == s[::-1]
    res=[]
    ans=[]
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if isPalindrome(s[i:j]):
                ans.append(s[i:j])
        res.append(ans[:])
        ans.clear()
    return res

print(partition('aab'))