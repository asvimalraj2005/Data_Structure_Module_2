Given an integer A. Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).

NOTE: 
   The value of A*A can cross the range of Integer.
   Do not use the sqrt function from the standard library. 
   Users are expected to solve this in O(log(A)) time.


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==0 or A==1:
            return A 
        ans=1
        l=1
        h=A 
        while(l<=h):
            m=(l+h)//2
            if(m*m==A):
                return m
            elif (m*m<A):
                ans=m
                l=m+1
            else:
                h=m-1
        return ans
