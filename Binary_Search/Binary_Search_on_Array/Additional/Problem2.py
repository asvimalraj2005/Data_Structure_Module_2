
Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

NOTE: Rows are numbered from top to bottom, and columns are from left to right.

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        n = len(A)
        if n == 0:
            return 0
        m = len(A[0])
        l, h = 0, m * n - 1
        
        while l <= h:
            mid = (l + h) // 2
            x = mid // m
            y = mid % m
            
            if A[x][y] == B:
                return 1
            elif A[x][y] < B:
                l = mid + 1
            else:
                h = mid - 1
        
        return 0
