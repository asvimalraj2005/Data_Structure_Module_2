Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max-height using these blocks.

The first stair would require only one block, and the second stair would require two blocks, and so on.

Find and return the maximum height of the staircase.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        l = 1
        h = A
        ans = 0
        while l <= h:
            mid = l + (h-l)//2

            if  mid * (mid + 1) // 2 <= A:
                ans = mid
                l = mid + 1
            else:
                h = mid -1
        return ans
