from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions):
        by_name = defaultdict(list)
        invalid = []
        for transaction in transactions:
            name, time, _, city = transaction.split(',')
            time = int(time)
            by_name[name].append((time, city))
        for transaction in transactions:
            # split了两次。1e3级别的split时间不长
            name, time, amount, city = transaction.split(',')
            time = int(time)
            amount = int(amount)
            if amount >= 1000:
                invalid.append(transaction)
                continue
            if all(city == other_city or abs(time - other_time) > 60
                   for other_time, other_city in by_name[name]):
                continue
            invalid.append(transaction)
        return invalid
