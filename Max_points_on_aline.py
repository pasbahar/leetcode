'''Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->'''
from math import gcd
def maxpoints(points):
    n=len(points)
    if n<2:
        return n
    maxpoint,curmax,overlap,vertical=0,0,0,0
    sloped={}

    for i in range(n):
        curmax,overlap,vertical=0,0,0

        for j in range(i+1,n):
            if points[i]==points[j]:
                overlap+=1
            elif points[i][0]==points[j][0]:
                vertical+=1
            else:
                ydif=points[j][1]-points[i][1]
                xdif=points[j][0]-points[i][0]
                g=gcd(ydif,xdif)

                ydif/=g
                xdif/=g
                if (ydif,xdif) not in sloped:
                    sloped[(ydif,xdif)]=0
                else:
                    sloped[(ydif,xdif)]+=1
                if sloped[(ydif,xdif)]>curmax:
                    curmax=sloped[(ydif,xdif)]
            if vertical>curmax:
                curmax=vertical
        if maxpoint<curmax+overlap+1:
            maxpoint=curmax+overlap+1
        sloped.clear()
    return maxpoint

points=[[-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [3, 4]]
print(maxpoints(points))
        
            



