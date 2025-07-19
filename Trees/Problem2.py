Given a binary tree, return the inorder traversal of its nodes' values.
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        if A is None:
            return []
        
        return self.inorderTraversal(A.left) + [A.val] + self.inorderTraversal(A.right)
