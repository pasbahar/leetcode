'''There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array obtained after
 merging the above 2 arrays(i.e. array of length 2n). The complexity should be O(log(n)).'''

def getMedian(arr1,arr2,n):
    if n==0: return-1
    elif n==1:
        return (arr1[0]+arr2[0])/2
    elif n==2:
        return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2
    else:
        m1=median(arr1,n)
        m2=median(arr2,n)
        if m1>m2:
            if n%2==0:
                return getMedian(arr1[:n//2+1],arr2[n//2-1:],n//2+1)
            else:
                return getMedian(arr1[:n//2+1],arr2[m//2:],n//2+1)
        else: 
            if n % 2 == 0: 
                return getMedian(arr1[int(n / 2 - 1):], 
                        arr2[:int(n / 2 + 1)], int(n / 2) + 1) 
            else: 
                return getMedian(arr1[int(n / 2):],  
                        arr2[0:int(n / 2) + 1], int(n / 2) + 1) 
def median(arr,n):
    if n%2==0:
        return (arr[n//2]+arr[n//2+1])/2
    else:
        return arr[n//2]