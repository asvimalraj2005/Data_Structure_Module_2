You are given a sorted array A of size N and a target value B.
Your task is to find the index (0-based indexing) of the target value in the array.

If the target value is present, return its index.
If the target value is not found, return the index of least element greater than equal to B.
If the target value is not found and least number greater than equal to target is also not present, return the length of array (i.e. the position where target can be placed)
Your solution should have a time complexity of O(log(N)).

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):

        left = 0
        right = len(A)-1


        while left <= right:


            mid = (left + right) // 2
           
            if A[mid] > B:
               
                right = mid - 1
           
            elif A[mid] < B:
                left = mid + 1

            elif A[mid] == B:

                return mid
        return left
