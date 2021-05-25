class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """ 动态规划  以二维表格存储匹配状态。 找到完全匹配的路径
        公式 1： p[j] == '?' and s[i-1]== p[j-1] 时 dp[i][j] = True
        公式 2： p[j] == '*' and (s[i] == p[j-1] or s[i-1] == p[j]) 时 dp[i][j] = True
        """
        sl = len(s)
        pl = len(p)
        dp = [[False] * (pl+1) for _ in range(sl+1)]
        dp[0][0] = True
        for j in range(1,pl+1):
            if  p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        for i in range(1,sl+1):
            for j in range(1,pl+1):
                if p[j-1] == '?' or s[i-1]==p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]
                
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """ 双指针  star 保存 * 坐标， match 匹配 * 号后的字母"""
        i,j = 0,0
        star = -1
        match = 0
        while i< len(s):
            if j<len(p) and (s[i] == p[j] or p[j] =='?') :
                i += 1
                j += 1
            elif j<len(p) and p[j] =='*':
                match = i
                star = j
                j += 1 
            elif star != -1:
                match += 1
                i = match
                j = star + 1
            else: return False
        # return ['*'] * len(p[j:]) == p[j:]
        return all(x == "*" for x in p[j:])         
                    


                    
                
