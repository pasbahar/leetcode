'''Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]'''

def dfs(res,nums,index,cur):
    n=len(nums)
    if index==n:
        res.append(cur[:])
        
        return
    dfs(res,nums,index+1,cur)#not pick current num

    #pick current num
    cur.append(nums[index])
    dfs(res,nums,index+1,cur)
    cur.clear()

def subsets(nums):
    res=[]
    dfs(res,nums,0,[])
    return res

print(subsets([1, 2, 3]))