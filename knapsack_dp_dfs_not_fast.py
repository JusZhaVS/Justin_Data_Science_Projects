class Solution:

    MOD = 10 ** 9 + 7

    def numberOfWays(self, n: int, x: int) -> int:
        powers = []
        i = 1

        while True:
            curr = pow(i, x)
            if curr > n:
                break
            powers.append(curr)
            i += 1

        #the typical dfs way doesn't work here
        dp = [0] * (n+1)
        dp[0] = 1

        for p in powers:
            for i in range(n, p-1, -1):
                dp[i] = (dp[i] + dp[i-p]) % self.MOD
        
        return dp[n]
