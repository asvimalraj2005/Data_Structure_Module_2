Farmer John has built a new long barn with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall and an integer B which represents the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        N = len(A)
        l = 1
        h = A[N - 1] - A[0]
        ans = 0

        while l <= h:
            M = l + (h - l) // 2
            if self.checkPossible(A, N, M, B):
                ans = M
                l = M + 1
            else:
                h = M - 1
        return ans

    def checkPossible(self, A, N, M, B):
        c = 1  # First cow is placed at A[0]
        lastpos = A[0]
        for i in range(1, N):
            if A[i] - lastpos >= M:
                c += 1
                lastpos = A[i]
                if c == B:
                    return True
        return False
