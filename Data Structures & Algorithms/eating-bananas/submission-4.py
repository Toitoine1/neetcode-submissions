import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        up = max(piles)
        while up != low + 1 :
            k = (up+low)//2
            print(up, low, k, sum((n//k)+1 for n in piles), sum((n//k)+1 for n in piles) <= h)
            if sum(math.ceil(n/k) for n in piles) <= h :
                up = k
            else :
                low = k
        print(up, low, up, sum((n//up)+1 for n in piles), sum((n//up)+1 for n in piles) <= h)
        return up