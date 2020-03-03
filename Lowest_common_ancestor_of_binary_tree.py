
'''Given a Binary Tree and 2 nodes value n1 and n2, your task is to find the lowest common ancestor(LCA) of the two nodes .
Note: Duplicates are not inserted in the BST.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains three lines of input.
The first line contains N, the number of nodes of the BST.
The second line contains the values of the nodes, each separated by a space.
The third line contains the two values n1 and n2 separated by a space.

Output Format:
For each testcase, in a new line, print the LCA of n1 and n2.

Your Task:
This is a function problem. You don't have to take any input. You are required to complete the function LCA() that takes node, n1, n2 as parameters and returns the node that is LCA of n1 and n2.

Constraints:
1 <= T <= 200
1 <= N <= 100
1 <= Node value <= 1000

Example:
Input
2
6
5 4 6 3 7 8
7 8
6
12 14 15 10 9 8
8 15

Output 
7
12

Explanation 
The BST in above test case will look like

    5
   /  \ 
  4  6
 /      \
3        7
            \ 
             8
here the LCA of 7 and 8 is 7.'''
  
def LCA(root,n1,n2):
    if not root: return None
    if root.key==n1 or root.key==n2:
        return root.key
    left=LCA(root.left,n1,n2)
    right=LCA(root.right,n1,n2)
    if left and right: return root.key
    elif left or right:
        return left if left else right
    else: return None


# Node Class:
class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

# Tree Class
class BSTree:
    def __init__(self):
        self.root = None

    def Insert(self,x):
        if self.root is None:
            self.root = Node(x)
            return
        curr_node = self.root
        while curr_node:
            if curr_node.key < x: # go to right subtree if value is more
                if curr_node.right is None:
                    break
                curr_node = curr_node.right
            elif curr_node.key > x:   #  go to left subtree if value is more.
                if curr_node.left is None:
                    break
                curr_node = curr_node.left
            else:
                return # no duplicate is to be inserted

        # insert key at the leaf position.
        if curr_node.key < x:
            curr_node.right = Node(x)
        else:
            curr_node.left = Node(x)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(int, input().strip().split()))  # parent child info in list
        n1,n2 = map(int, input().strip().split())
        # construct the tree according to given list
        tree = BSTree()
        for value in a:
            tree.Insert(value)  # Insert the nodes in tree.
        print(LCA(tree.root,n1,n2))