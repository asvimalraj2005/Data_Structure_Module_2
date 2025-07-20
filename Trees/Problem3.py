Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
from collections import deque

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        q=deque()
        ans=[]
        node=A
        q.append(node)

        while len(q):
            lengthOfQ = len(q)
            res=[]
            while lengthOfQ:
                poppedEl = q.popleft()
                res.append(poppedEl.val)
                if poppedEl.left:
                    q.append(poppedEl.left)
                if poppedEl.right:
                    q.append(poppedEl.right)
                lengthOfQ-=1
            ans.append(res)
        return ans
