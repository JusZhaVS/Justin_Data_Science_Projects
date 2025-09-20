from typing import List, DefaultDict
from collections import defaultdict

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}
        n = len(prices)

        def dfs(i, buying):

            #do base cases first here, which are out of bounds or if alr computed

            if i >= len(prices): #if index goes out of bounds, "empty" array of prices so no profit
                return 0 
            
            if (i, buying) in dp: #if already cached before
                return dp[(i, buying)]
            
            if buying:
                #we can 
                buy = dfs(i+1, False) - prices[i] #bought, so have to subtract prices[i]
                cooldown = dfs(i+1, True)
                #DON'T FORGET TO CAHCE
                dp[(i, buying)] = max(buy, cooldown)
            else: #we're selling in this case
                sell = dfs(i+2, True) + prices[i] #have to cooldown, so jump by 2
                cooldown = dfs(i+1, False)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)
