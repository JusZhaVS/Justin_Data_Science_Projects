#top down solution

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = {}

        def dfs(i, j): #position i in s, position j in p
            if (i,j) in dp:
                return dp[(i,j)] #memoization/caching
            
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".") #check if the current chars match, also have to check in bounds first

            if (j+1) < len(p) and p[j+1] == "*": #first char in pattern string will never be star
                dp[(i,j)] = dfs(i, j + 2) or (match and dfs(i+1, j)) 
                return dp[(i,j)] #don't use star, add 2 to jump past star as well, or use star, then keep going 
            
            if match:
                dp[(i,j)] = dfs(i+1, j+1)
                return dp[(i,j)]
            
            dp[(i,j)] = False
            return dp[(i,j)]
        

        return dfs(0,0)