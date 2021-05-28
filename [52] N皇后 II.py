class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, left, right):
            """
            :queens
            """
            q = len(queens)
            if q == n: 
                res.append(queens)
                return
            for j in range(n):
                # 皇后不在出线皇后的列 queens，
                # 皇后不在出现皇后的左对角线 left, （行索引-列索引）固定值， 对应左下斜对角
                # 皇后不在出现皇后的右对角线 right,（行索引+列索引）固定值， 对应右下对角
                if j not in queens and q-j not in left and q+j not in right:  
                    dfs(queens+[j], left+[q-j], right+[q+j])
        res =[]            
        dfs([],[],[])
        return len(res)