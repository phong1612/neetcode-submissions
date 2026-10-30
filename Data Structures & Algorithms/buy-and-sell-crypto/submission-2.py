class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggest_day = [prices[-1]]*len(prices)
        max_prof = 0
        for i in range(len(prices) - 2, -1, -1):
            biggest_day[i] = max(biggest_day[i + 1], prices[i])
        for i in range(len(prices)):
            max_prof = max(biggest_day[i] - prices[i], max_prof)
        return max_prof