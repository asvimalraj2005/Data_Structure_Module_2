Given two sorted arrays A and B of size M and N respectively, return the median of the two sorted arrays.
Round of the value to the floor integer [2.6=2, 2.2=2]

def find_median_sorted_arrays(A, B):
    merged = sorted(A + B)
    total_len = len(merged)

    if total_len % 2 == 1:
        # Odd length: middle element is the median
        return merged[total_len // 2]
    else:
        # Even length: average of two middle elements, use integer division to floor
        mid1 = merged[total_len // 2 - 1]
        mid2 = merged[total_len // 2]
        return (mid1 + mid2) // 2  # This automatically floors the result
