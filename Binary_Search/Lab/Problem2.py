Given a sorted array of integers A of size N and an integer B, 
where array A is rotated at some pivot unknown beforehand.

For example, the array [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

Your task is to search for the target value B in the array. If found, return its index; otherwise, return -1.

You can assume that no duplicates exist in the array.

NOTE: You are expected to solve this problem with a time complexity of O(log(N)).

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        low = 0
        high = len(A) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B:
                return mid
            
            # Left half is sorted
            if A[low] <= A[mid]:
                if A[low] <= B < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if A[mid] < B <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1
