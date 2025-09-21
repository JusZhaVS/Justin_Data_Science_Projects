#turns standard 2D table into a 1D row
#we do the m,n swap because only the shorter string's length determines the row size in memory.
#swapping ensures we allocate O(min(m,n)) space

#good explanation here: https://chatgpt.com/c/68d04e1a-a850-8325-adbe-8cb31b2e7225

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        if m < n:
            m,n = n,m
            word1, word2 = word2, word1

        dp = [(n-i) for i in range(n+1)] #bottom row of the 2D DP table

        for i in range(m-1, -1, -1):
            nextDp = dp[n] #going to hold the dp2[i+1][j+1] values
            dp[n] = m - i #right column of the 2D DP table
            for j in range(n-1, -1, -1):
                temp = dp[j] #to store in nextDp, because this is the previous row's val
                if (word1[i] == word2[j]):
                    #dp[j] = dp[j+1] THIS IS WRONG, SHOULD BE NEXTDP
                    dp[j] = nextDp
                else:
                    dp[j] = 1 + min(dp[j], dp[j+1], nextDp)
                nextDp = temp

        return dp[0]
