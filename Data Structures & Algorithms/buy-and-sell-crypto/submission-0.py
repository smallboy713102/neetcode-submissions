class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        maxProfit = 0
        currProfit = 0

        i = 0
        j = 1

        while j < n:

            if prices[j] < prices[i]:
                i = j
                j += 1

            else:
                currProfit = prices[j] - prices[i]
                maxProfit = max(maxProfit, currProfit)
                j += 1

        return maxProfit