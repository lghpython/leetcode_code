class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        回溯法
        1. 查找第一个字符 记录坐标（i,j) 不再利用
        2. 上下左右查找下一个字母 i-1, j-1 j+1 j-1
        3. 除了上个字母的其他三个方向查找
        4. 找不到，删除记录坐标， 重新从第一个字母开始
        """
        m = len(board) # 行数
        n = len(board[0]) # 列数
        w = len(word)
        
        if m==1 or n==1: 
            wstr = "".join(word)
            bstr = ''.join(''.join(b) for b in board)
            return wstr in bstr or wstr[::-1] in bstr  
        def dfs(i, j, which, record):
            if board[i][j] == word[which] and (i,j) not in record:
                record.append((i,j))
                if which == w-1:return True 
            else: 
                return
            # 上下左右， 查找
            if i<m-1 and (i+1,j) not in record and dfs(i+1,j, which+1,record) \
            or j<n-1 and (i,j+1) not in record and dfs(i,j+1, which+1,record) \
            or i>0 and (i-1,j) not in record and dfs(i-1,j, which+1,record) \
            or j>0 and (i,j-1) not in record and dfs(i,j-1, which+1,record):
                return True
            else:
                record.pop()

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0,[]): return True 
        return False


# [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
# "AAAAAAAAAAAAAAB"