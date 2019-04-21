import itertools

class Solution:

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        def get_distance(point1):
            return abs(point1[1]-c0)+ abs(point1[0]-r0)

        it = itertools.product(range(R),range(C))
        return sorted(list(it), key = get_distance)

