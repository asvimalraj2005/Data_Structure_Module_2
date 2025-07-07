Given an array of integers A of size N and an integer B.

The College library has N books. The ith book has A[i] number of pages.

You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.

class Solution:
    def check(self, A, mid, B) :
        pages = 0
        students = 1
        for i in range(len(A)) :
            if pages + A[i] <= mid :
                pages += A[i]
            else :
                pages = A[i]
                students += 1
        if students > B :
            return False
        return True

    def books(self, A, B):
        n = len(A)
        l = max(A)
        r = sum(A)
        if B > n :
            return -1
        ans = -1
        while l <= r :
            mid = (l + r) // 2
            if self.check(A, mid, B) :
                ans = mid
                r = mid - 1
            else :
                l = mid + 1
        return ans
