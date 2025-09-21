class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        dp = [ [float("INF")] * (m + 1) for _ in range(n+1)]
        #dp[i][j] represents what is distance after first i, first j filled

        for i in range(n+1):
            dp[i][m] = n - i
        for j in range(m+1):
            dp[n][j] = m - j

        #bottom up DP
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if (word1[i] == word2[j]):
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        return dp[0][0]
