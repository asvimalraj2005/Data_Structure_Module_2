Given an integer array A of size N.

If we store the sum of each triplet of the array A in a new list, then find the B-th smallest element among the list.

NOTE: A triplet consists of three elements from the array. Let's say if A[r1], A[r2], A[r3] are the elements of the triplet, then r1 < r2 < r3.

def find_bth_smallest_triplet_sum(A, B):
    N = len(A)
    triplet_sums = []

    # Generate all triplets and their sums using v, r, s
    for r1 in range(N):
        for r2 in range(r1 + 1, N):
            for r3 in range(r2 + 1, N):
                triplet_sums.append(A[r1] + A[r2] + A[r3])
    
    # Sort the list of triplet sums
    triplet_sums.sort()

    # Return the B-th smallest sum (1-based index)
    return triplet_sums[B - 1]

