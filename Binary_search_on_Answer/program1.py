Given 2 integers A and B and an array of integers C of size N. Element C[i] represents the length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of the board.

Calculate and return the minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of the board.
NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.

Return the ans % 10000003.


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        for i in range(len(C)):
            C[i]=C[i]*B
        l=max(C)
        h=sum(C)
        ans=-1
        N=len(C)
        while(l<=h):
            mid=l+(h-l)//2
            if self.checkpossible(A,N,mid,C):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans%10000003
    
    def checkpossible(self,A,N,M,C):
        P=1
        currSum=0
        for i in range(N):
            currSum=currSum+C[i]
            if currSum>M:
                currSum=C[i]
                P=P+1
        return (P<=A)

