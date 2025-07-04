Given an array of integers A, find and return the peak element in it.
An array element is considered a peak if it is not smaller than its neighbors. For corner elements, we need to consider only one neighbor.

NOTE:

It is guaranteed that the array contains only a single peak element.
Users are expected to solve this in O(log(N)) time. The array may contain duplicate elements.



  class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N=len(A)
        if N==1 or A[0]>=A[1]:
            return A[0]
        elif A[N-1]>=A[N-2]:
            return A[N-1]
        l=1
        h=N-2
        while(l<=h):
            m=(l+h)//2
            if (A[m]>A[m-1] and A[m]>A[m+1]):
                return A[m]
            elif A[m-1]>A[m]:
                h=m-1
            else:
                l=m+1
        
