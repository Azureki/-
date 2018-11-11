class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        for log in logs:

            tem = log.split(' ', 1)
            if tem[1][0].isdigit():
                digit_logs.append(tem)
            else:
                letter_logs.append(tem)
        letter_logs.sort(key=lambda t: t[1])
        return [' '.join(s) for s in letter_logs] + [' '.join(s) for s in digit_logs]


s = Solution()
print(s.reorderLogFiles(logs))
