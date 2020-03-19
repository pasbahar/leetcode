from heapq import *

def topKFrequent(nums, k):
    
    d={}
    heap=[]
    res=[]
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d.values():
        heap.append(-i)
    heapify(heap)
    for i in range(k):
        tmp=heap.pop(0)
        heapify(heap)
        for val,freq in d.items():
            if freq==-tmp:
                res.append(val)
                break       
        del d[res[len(res)-1]]         
    return res

print(topKFrequent([5,2,5,3,5,3,1,1,3],2))