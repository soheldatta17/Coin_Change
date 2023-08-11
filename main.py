class Solution:
    def count(self, coins, N, sum):
        dp = [[0 for x in range(N)] for x in range(sum+1)]
    
        for i in range(N):
            dp[0][i] = 1
        
    
        for i in range(1, sum+1):
            for j in range(N):
                dp[i][j] = (dp[i - coins[j]][j] if i-coins[j] >= 0 else 0) + (dp[i][j-1] if j-1 >=0 else 0)
        return dp[sum][N-1]