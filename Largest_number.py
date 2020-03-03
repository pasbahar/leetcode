'''Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"'''

class largenumkey(str):
    def __lt__(x,y):
        return x+y>y+x

class Solution:
    def largestnum(self,nums):
        largetsnum=''.join(sorted(map(str,nums),key=largenumkey))
        return '0' if largetsnum[0]=='0' else largetsnum