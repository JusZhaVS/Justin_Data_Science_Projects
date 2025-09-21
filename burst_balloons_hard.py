#depends on which balloon to pop last

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1] #do padding with 1s on end
        dp = {}

        def dfs(l: int, r: int) -> int: #the left and right boundaries
            #some base cases to take care of first
            if (l > r):
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)] = 0
            for i in range(l, r + 1): #doing caeswork on which one of them is the last one to be popped
                curr_coins = nums[l-1] * nums[i] * nums[r+1]
                curr_coins += dfs(l, i - 1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], curr_coins)

            return dp[(l,r)]

        return dfs(1, len(nums) - 2) #the len of the news nums here - 2
