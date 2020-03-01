'''Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.'''
def intersect(nums1,nums2):
    d={}
    res=[]
    for i in nums1:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for i in nums2:
        if i in d.keys():
            if d[i]:
                d[i]-=1
                res.append(i)
    return res

print(intersect([1,2,2,1],[2,2]))