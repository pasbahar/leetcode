'''Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.'''
def flip(arr,k):
    for i in range(k//2):
        arr[i],arr[k-1-i]=arr[k-1-i],arr[i]
 
    
def pancake_sort(arr):
  pass # your code goes here
  for i in range(len(arr)):
    flip(arr,arr.index(max(arr[:len(arr)-i]))+1)
    flip(arr, len(arr)-i)

arr= list(map(int,input().split()))
pancake_sort(arr)
print (arr)