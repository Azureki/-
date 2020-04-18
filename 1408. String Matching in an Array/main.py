class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        length = len(words)
        for i in range(length):
            for j in range(length):
                if i!=j and (words[i] in words[j]):
                    res.append(words[i])
                    break
        return res
