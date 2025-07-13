
Given a matrix of integers A of size N x M in which each row is sorted.


Find and return the overall median of matrix A.

NOTE: No extra memory is allowed.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        def countLessEqual(val, row):
            """Return the number of elements <= val in a sorted row using binary search."""
            low, high = 0, len(row)
            while low < high:
                mid = (low + high) // 2
                if row[mid] <= val:
                    low = mid + 1
                else:
                    high = mid
            return low

        rows = len(A)
        cols = len(A[0])
        total_elements = rows * cols
        required = (total_elements // 2) + 1

        # Find global min and max
        min_val = min(row[0] for row in A)
        max_val = max(row[-1] for row in A)

        ans = 0
        left, right = min_val, max_val

        while left <= right:
            mid = (left + right) // 2
            count = sum(countLessEqual(mid, row) for row in A)

            if count >= required:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
