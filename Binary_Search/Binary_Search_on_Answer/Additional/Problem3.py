Given an array of integers A of size N and an integer B.

In a single operation, any one element of the array can be increased by 1. You are allowed to do at most B such operations.

Find the number with the maximum number of occurrences and return an array C of size 2, where C[0] is the number of occurrences, and C[1] is the number with maximum occurrence.
If there are several such numbers, your task is to find the minimum one.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def check(self, count, B, A, i, prefix):
        if (A[i]*count)-(prefix[i+1]-prefix[i-count+1])<=B:
            return True
        return False

    def solve(self, A, B):
        A=sorted(A)
        n=len(A)
        prefix=[0]
        for i in range(len(A)):
            prefix.append(prefix[i]+A[i])

        ans=[-1, -1]
        for i in range(len(A)):
            low=1
            high=i+1
            while low<=high:
                count=(low+high)//2
                if self.check(count, B, A, i, prefix):
                    mx=count
                    low=count+1
                else:
                    high=count-1
           
            if ans[0]<mx:
                ans[0]=mx
                ans[1]=A[i]
        return ans
