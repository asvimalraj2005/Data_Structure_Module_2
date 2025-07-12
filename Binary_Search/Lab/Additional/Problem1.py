You are given a 2-D matrix C of size A × B.
You need to build a new 1-D array of size A by taking one element from each row of the 2-D matrix in such a way that the cost of the newly built array is minimized.

The cost of an array is the minimum possible value of the absolute difference between any two adjacent elements of the array.

So if the newly built array is X, the element picked from row 1 will become X[1], element picked from row 2 will become X[2], and so on.

Determine the minimum cost of the newly built array.

  def bsearch(l, r, target, arr):

    while l < r:

        mid = (l + r) // 2

        if target == arr[mid]:

            return mid

        elif target > arr[mid]:

            l = mid+1

        else:

            r = mid - 1

    return l


class Solution:

    # @param A : integer

    # @param B : integer

    # @param C : list of list of integers

    # @return an integer

    def solve(self, A, B, C):

            n = A

            m = B

            mat = C

            for i in range(n):

                mat[i].sort()

            ans = float('inf')

            for i in range(n - 1):

                for j in range(m):

                    index = bsearch(0, m - 1, mat[i][j], mat[i + 1])

                    ans = min(ans, abs(mat[i][j] - mat[i + 1][index]))

                    if index !=0:

                        ans = min(ans, abs(mat[i][j] - mat[i + 1][index-1]))

            return ans
