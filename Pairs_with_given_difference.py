'''Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []'''
def find_pairs_with_given_difference(arr, k):
    pass # your code goes here
    d={}
    res=[]
    pair=[0]*2
    for i in arr:
        d[i-k]=i
    for i in arr:
        if i in d.keys():
            pair[0]=d[i] 
            pair[1]=i
            res.append(pair[:])
    return res


arr=list(map(int, input().split()))
k=int(input())
print(find_pairs_with_given_difference(arr,k))