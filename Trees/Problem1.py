Problem Description

Given a Binary Search Tree A. Check whether there exists a node with value B in the BST.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        while A != None:
            if A.val == B:
                return 1
            elif A.val > B:
                A = A.left
            elif A.val < B:
                A = A.right
        return 0
        
