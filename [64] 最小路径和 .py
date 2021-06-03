class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """回溯法， 超时"""
        m,n = len(grid), len(grid[0])
        ans = m*n*100
        def dfs(x,y,sum):
            nonlocal ans
            if x == m-1 and y == n-1:
                ans = min(ans,sum+grid[x][y])
                return
            if y<n-1: dfs(x,y+1,sum+grid[x][y])
            if x<m-1: dfs(x+1,y,sum+grid[x][y])
            return
        dfs(0,0,0)
        return ans

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """动态规划"""
        m,n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)] 
        dp[0][0] = grid[0][0]
        for x in range(1,m):
            dp[x][0] = dp[x-1][0]+grid[x][0]
        for y in range(1,n):
            dp[0][y] = dp[0][y-1]+grid[0][y]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]