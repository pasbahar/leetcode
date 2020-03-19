import sys
#min value
a=-sys.maxsize-1


def threesum(nums):
    res=set()
    nums.sort()
    for j in range(0,len(nums)):
        l=j+1
        r=len(nums)-1
        while(l<r):
            sumof3=nums[j]+nums[l]+nums[r]
            if sumof3==0:
                res.add((nums[j],nums[l],nums[r]))
                l+=1
                r-=1
            elif sumof3<0:
                l+=1
            else:
                r-=1  
    return list(res)

print(threesum([-1,0,1,2,-1,-4]))