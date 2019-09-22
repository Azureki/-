class Solution:
    def nthUglyNumber(self, n, a, b, c):
        gcd = lambda x, y: (gcd(y, x % y) if x % y else y)

        # lcm = lambda x, y: x * y // gcd(x, y)
        def lcm(x, y, *args):
            if not args:
                return x * y // gcd(x, y)
            x = lcm(x, y)
            y, *args = args
            return lcm(x, y, *args)

        a, b, c = sorted([a, b, c])
        max_n = 2 * 10**9 + 1
        left, right = 0, max_n
        mid = 0

        def get_ugly_num():
            get_one = lambda x: mid // x
            get_two = lambda x, y: mid // lcm(x, y)
            num_a, num_b, num_c = get_one(a), get_one(b), get_one(c)
            num_a_b, num_b_c, num_a_c = get_two(a, b), get_two(b, c), get_two(a, c)
            num_a_b_c = mid // lcm(a, b, c)
            return num_a + num_b + num_c - num_a_b - num_a_c - num_b_c + num_a_b_c

        while left < right:
            mid = (left + right) // 2
            ugly_num = get_ugly_num()
            if ugly_num < n:
                left = mid + 1
            else:
                right = mid

        return left
