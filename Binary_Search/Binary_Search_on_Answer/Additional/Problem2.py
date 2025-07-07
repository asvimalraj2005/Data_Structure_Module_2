Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with the sum of elements greater than B.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        s = 0
        e = n
        ans = s
        while s <= e:
            mid = s + ((e-s)//2)
            if self.is_possible(n, A, B, mid):
                ans = mid
                s = mid + 1
            else:
                e = mid - 1
        return ans
   
    def is_possible(self, n , A, B, mid):
        elsum = 0
        for i in range(mid):
            elsum += A[i]
            if elsum > B:
                return False
       
        s = 1
        e = mid
        while e < n:
            elsum -= A[s-1]
            elsum += A[e]
            if elsum > B:
                return False
            s += 1
            e += 1
        return True
