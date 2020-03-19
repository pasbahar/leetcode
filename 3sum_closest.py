def threesum(nums,target):
    res=set()
    nums.sort()
    minsum=10000
    ans=0
    for j in range(0,len(nums)):
        l=j+1
        r=len(nums)-1
        while(l<r):
            sumof3=nums[j]+nums[l]+nums[r]
            dist=sumof3-target
            if minsum>abs(dist):
                minsum=abs(dist)
                ans=sumof3
            if sumof3==target:
                return target 
            elif sumof3<target:
                l+=1
            else:
                r-=1    
    return ans

print(threesum([1,1,1,0],-100))