Given a sorted array of integers A (0-indexed) of size N, find the left most and the right most index of a given integer B in the array A.

Return an array of size 2, such that 
          First element = Left most index of B in A
          Second element = Right most index of B in A.
If B is not found in A, return [-1, -1].

Note : Note: The time complexity of your algorithm must be O(log n)..


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        if B not in A:
            return [-1, -1]
        Right=self.index_right(A,B)
        Left=self.index_left(A,B)
        return [Left,Right]
    
    def index_left(self,A,B):
        l=0
        r=len(A)-1
        ans=0
        while(l<=r):
            mid=l+(r-l)//2
            if A[mid]==B:
                ans=mid
                r=mid-1
            elif A[mid]<B:
                l=mid+1
            else:
                r=mid-1
        return ans
    
    def index_right(self,A,B):
        l=0
        r=len(A)-1
        N=len(A)
        ans=0
        while(l<=r):
            mid=l+(r-l)//2
            if A[mid]==B:
                ans=mid
                l=mid+1
            elif A[mid]<B:
                l=mid+1
            else:
                r=mid-1
        return ans

