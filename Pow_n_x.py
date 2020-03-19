'''Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25'''

def fast(x,n):
    if n==0:return 1.0;
    half=fast(x,n/2)
    if n%2==0: return half*half
    else: return half*half*x

def mypow(x,n):
    if N<0:
        x=1/x
        n=-n
    return fast(x,N)

