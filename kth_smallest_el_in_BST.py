'''Given root of binary search tree and K as input, find K-th smallest element in BST. Your task is to return the K-th smallest element in BST from the function k_smallest_element().

Note: The Time Complexity will be O(h) where h is the height of the Tree.

Input:
The first line of input will contain the number of test cases T. Then T test cases follow. First line of every test case will be n, denoting the number of nodes in the BST. Second line of every test case will be n spaced integers denoting the Integer value of Nodes in BST. Third line of every test case will be k, denoting kth the smallest number.

Output:
For each test case, output will be the kth smallest element of BST.

Constraints:
1<=T<=100
1<=N<=100
1<=K<=N


Example(To be used only for expected output):
Input:
1
5
20 8 4 22 12
3 
Output:
12'''

# your task is to complete this function
# function should return kth smallest element from the BST
def util(root,k,count,val):
    if not root: return
    util(root.left,k,count,val)
    count[0]+=1
    if count[0]==k: 
        val[0]=root.data 
    util(root.right,k,count,val)  

def k_smallest_element(root, n):
    count=[0]
    val=[0]
    util(root,n,count,val)
    return val




#{ 
#  Driver Code Starts
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k

def insert_node(root, node):
    # print root, node
    ptraverse = root
    curparent = root
    while(ptraverse != None):
        curparent = ptraverse
        if node.data<ptraverse.data:
            ptraverse.key+=1
            ptraverse=ptraverse.left
        else:
            ptraverse=ptraverse.right
    if root is None:
        root = node
    elif node.data<curparent.data:
        curparent.left=node
    else:
        curparent.right=node
    return root

def build_bst(root, arr, n):
    for it in range(n):
        root = insert_node(root, Node(arr[it], 0))
    return root
    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root= None
        root = build_bst(root, arr, n)
        k = int(input())
        print(k_smallest_element(root, k))
# Contributed by: Harshit Sidhwa

# } Driver Code Ends