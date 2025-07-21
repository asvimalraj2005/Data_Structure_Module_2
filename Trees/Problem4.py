Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).

Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        return self.createBST(A, 0, len(A) - 1)

    def createBST(self, nums,s,e):
        if s > e:
            return None
        mid = (s + e )//2
        newTree = TreeNode(nums[mid])
        newTree.left = self.createBST(nums,s,mid-1)
        newTree.right = self.createBST(nums,mid+1,e)
        return newTree
