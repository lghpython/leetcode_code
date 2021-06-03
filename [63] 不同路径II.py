class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] ==1:
            return 0
        import numpy as np 
        m,n = np.shape(obstacleGrid)
        d = [[1] * n] + [[1] + [0] * (n-1) for _ in range(m-1)]
        for i in range(m):
            for j in range(n):
                
                if obstacleGrid[i][j] ==1:
                    d[i][j] = -1
                if d[i-1][0] == -1 and i>0:
                    d[i][0] = -1
                if d[0][j-1]==-1 and j >0:
                    d[0][j] = -1
                    
        for i in range(1,m):
            for j in range(1,n):
                if d[i][j] != -1:
                    if d[i-1][j] ==-1 and d[i][j-1]==-1:
                        d[i][j] = -1
                    elif d[i-1][j]==-1:
                        d[i][j] = d[i][j-1]
                    elif d[i][j-1]==-1:
                        d[i][j] = d[i-1][j]
                    else:
                        d[i][j] = d[i-1][j] + d[i][j-1]
        if d[0][0] <0 or d[m-1][n-1] <0: return 0
        return d[m-1][n-1] if d[m-1][n-1] !=-1 else 0
                

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] ==1 :
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)] 
        
        for x in range(m):
            if obstacleGrid[x][0] == 0:
                dp[x][0]=1
            else:
                break
        for y in range(n):
            if obstacleGrid[0][y] == 0:
                dp[0][y]= 1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    print(i,j,dp[i-1][j] , dp[i][j-1])
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
                
        

        
        

        