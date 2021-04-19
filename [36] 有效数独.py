class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """去重验证长度"""
        for x in range(9):
            raw = []
            col = []
            area=[]
            for y in range(9):
                # 提取每行
                if board[x][y] != '.':
                    raw.append(board[x][y])
                # 提取每列
                if board[y][x]!= '.':
                    col.append(board[y][x])
                # 提取每九方格
                xx = (x//3)*3 + y//3
                yy = (x%3)*3 + y%3
                
                if board[xx][yy] != '.':
                    area.append(board[xx][yy])
                    

            # 验证 去重后 长度
            if len(set(raw)) != len(raw) or len(set(col)) != len(col) or len(set(area)) != len(area): 
                return False
        
        return True
 
 
 class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows  = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        area = [set() for _ in range(9)]
        for x in range(9):
            for y in range(9):
                item = board[x][y]
                pos = (x//3)*3 + y//3
                if item != '.':
                    if item not in rows[x] and item not in cols[y] and item not in area[pos]:
                        rows[x].add(item)
                        cols[y].add(item)
                        area[pos].add(item)
                    else: return False
        return True