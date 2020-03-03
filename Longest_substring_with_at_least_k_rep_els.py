'''Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.'''
def util(s,k,l,r,maxlen):
            flag=0
            if l>=r:
                return
            d={}
            for i in range(l,r):
                if s[i] in d.keys():
                    d[s[i]]+=1
                else:
                    d[s[i]]=1
            for i in range(l,r):
                if d[s[i]]<k:
                    flag=1
                    if i-k>=k:
                        util(s,k,l,i-1,maxlen)
                    if r-i-1>=k:
                        util(s,k,i+1,r,maxlen)
            if not flag and r-l>maxlen[0]:
                maxlen[0]=r-l
                return

    
def longestSubstring(s, k):
    maxlen=[0]
    
    
    util(s,k,0,len(s),maxlen)
    return maxlen[0]

print(longestSubstring("abcdedghijklmnopqrs",2))