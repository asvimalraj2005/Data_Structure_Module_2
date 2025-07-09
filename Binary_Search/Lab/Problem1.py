Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

Elements which are appearing twice are adjacent to each other.

NOTE: Users are expected to solve this in O(log(N)) time.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        if N == 1:
            return A[0]
        if A[0] != A[1]:
            return A[0]
        if A[N - 1] != A[N - 2]:
            return A[N - 1]

        l = 0
        h = N - 1  # fix: was N, should be N - 1

        while l <= h:
            mid = l + (h - l) // 2

            if self.is_unique(A, mid):
                return A[mid]

            # Check if mid is part of a pair and adjust accordingly
            if mid + 1 < N and A[mid] == A[mid + 1]:
                if mid % 2 == 0:
                    l = mid + 2
                else:
                    h = mid - 1
            elif mid - 1 >= 0 and A[mid] == A[mid - 1]:
                if (mid - 1) % 2 == 0:
                    l = mid + 1
                else:
                    h = mid - 2

    def is_unique(self, A, mid):
        N = len(A)
        if mid == 0:
            return A[mid] != A[mid + 1]
        if mid == N - 1:
            return A[mid] != A[mid - 1]
        return A[mid] != A[mid - 1] and A[mid] != A[mid + 1]
