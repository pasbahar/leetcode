'''Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.'''

from collections import deque

def numsquares(n):
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i*i)
            i+=1
        
        queue = deque([0])
        
        cntOfStep = 0
        popLen = 1
        nextPopLen = 0
        while queue:
            cntOfStep += 1
            while popLen > 0:
                node = queue.popleft()
                for square in squares:
                    tmp = node + square
                    if tmp == n:
                        return cntOfStep
                    elif tmp < n:
                        queue.append(tmp)
                        nextPopLen += 1
                    else:
                        break
                popLen -= 1
            popLen = nextPopLen
            nextPopLen = 0
        return cntOfStep
     

print(numsquares(12))