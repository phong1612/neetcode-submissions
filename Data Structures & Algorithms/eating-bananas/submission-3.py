class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        best = right
        while left <= right:
            mid_rate = (left + right) // 2
            sum = 0
            for pile in piles:
                sum += math.ceil(pile / mid_rate)
            if sum <= h:
                best = mid_rate if mid_rate < best else best
                right = mid_rate - 1
            else:
                left = mid_rate + 1
        return best