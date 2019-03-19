class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        """
        解法：二分搜索
        target = D，也就是说，当天数恰好为D时，返回重量。
        """

        def count_days(weight):
            """
            当重量为weight时，返回需要的天数
            """
            if weight < mi:
                return D + 1
            count = 1
            tem = weight
            for x in weights:
                if tem >= x:
                    tem -= x
                else:
                    count += 1
                    tem = weight - x
            return count

        def bin_search(low, high):
            if low > high:
                return low
            mid = (low + high) // 2
            days = count_days(mid)
            print(mid, days)
            if days <= D:
                return bin_search(low, mid - 1)
            else:
                return bin_search(mid + 1, high)

        if len(weights) < D:
            return max(weights)
        mi = max(weights)
        ma = sum(weights)
        return bin_search(mi, ma)

