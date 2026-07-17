# DP, keep track of the minimum element from all previous of the current element
# Think and easy only yk

class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        profit=0
        for i in range (1,len(prices)):
            cost=prices[i]-mini
            mini=min(mini,prices[i])
            profit=max(profit,cost)
        return profit

# Time-complexity: O(N)
# Space-complexity: O(1)