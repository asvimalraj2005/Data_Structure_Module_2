You are given three positive integers, A, B, and C.

Any positive integer is magical if divisible by either B or C.

Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.

Note: Ensure to prevent integer overflow while calculating.

class Solution:
    # Helper function to calculate gcd
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    # Main function
    def solve(self, A, B, C):
        MOD = 10**9 + 7

        def lcm(x, y):
            return (x * y) // self.gcd(x, y)

        def count_magical(x):
            return (x // B) + (x // C) - (x // lcmBC)

        lcmBC = lcm(B, C)
        low, high = 1, A * min(B, C)

        while low < high:
            mid = (low + high) // 2
            if count_magical(mid) < A:
                low = mid + 1
            else:
                high = mid

        return low % MOD

