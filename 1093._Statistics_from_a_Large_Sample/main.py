from bisect import bisect_left


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mode = count.index(max(count))
        min_v, max_v = 0, 0
        for i, x in enumerate(count):
            if x != 0:
                min_v = i
                break
        for i in range(len(count) - 1, -1, -1):
            if count[i] != 0:
                max_v = i
                break
        SUM, num = 0, 0
        for i, x in enumerate(count):
            SUM += i * x
            num += x

        count_sum = count[:]
        for i in range(1, len(count_sum)):
            count_sum[i] = count_sum[i] + count_sum[i - 1]

        is_odd = lambda x: x & 1
        mid = bisect_left(count_sum, num // 2)
        if is_odd(num):
            median = mid
        elif count_sum[mid] != num // 2:
            median = mid
        else:
            mid_next = bisect_left(count_sum, num // 2 + 1)
            median = (mid + mid_next) / 2
        return (min_v, max_v, SUM / num, median, mode)
