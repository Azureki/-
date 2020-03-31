class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for n in (0, 1):
            length = len(rating)
            for i in range(0, length-2):
                for j in range(i+1, length-1):
                    for k in range(j+1, length):
                        if n == 0 and rating[i] < rating[j] < rating[k]:
                            res+=1
                        elif n == 1 and rating[i] > rating[j] > rating[k]:
                            res+=1
        return res

