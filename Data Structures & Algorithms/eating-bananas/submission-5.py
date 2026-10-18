import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        up = max(piles)
        while up != low + 1 :
            k = (up+low)//2
            if sum(math.ceil(n/k) for n in piles) <= h :
                up = k
            else :
                low = k
        return up