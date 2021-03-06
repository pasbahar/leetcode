'''Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.'''    
def canJump(nums):
    if len(nums)==1: return True
    fr=0
    for i in range(len(nums)):
        if nums[i]+i>fr:
            fr=nums[i]+i
        if i+1>fr and i+1!=len(nums):
            return False
    return True
    
print(canJump([2,1,1,1,4]))