from typing import Collection


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(pos:int):
            nonlocal valid
            if pos == len(dots):
                valid = True
                return 
            i,j = dots[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i//3][j//3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i//3][j//3][digit] = True
                    board[i][j] = str(digit+1)
                    dfs(pos+1)
                    line[i][digit] = column[j][digit] = block[i//3][j//3][digit] = False
                if valid:
                    return

        ## 按下标对应的位置（下标从0开始对应+1的数），标记该数是否使用
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        dots = list()
        ## 遍历board数独， 将已知的数字，在对应的line， column ， block列表中 
        ## 按下标对应的位置（下标从0开始对应+1的数） 标记为True 
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    dots.append((i,j))
                else:
                    digit = int(board[i][j])-1
                    line[i][digit] = column[j][digit] = block[i//3][j//3][digit] = True
        dfs(0)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 通过 对1 左移digit位， 来保存 digit +1 数字 已出现
        def flip(i:int, j:int, digit:int):
            line[i] ^= (1<<digit)
            column ^= (1<<digit)
            block[i//3][j//3] ^= (1<<digit)

        def dfs(pos:int):
            nonlocal valid
            if pos == len(dots):
                valid = True
                return 
            i,j = dots[pos]
            mask = ~(line[i] | column[j] | block[i//3][j//3]) & 0x1FF
            while mask:
                digitmask = mask & (-mask)  # 表示中最低位的 11, 负数补码（取反+1）
                digit = bin(digitmask).count('0')-1
                flip(i,j,digit)
                board[i][j] = str(digit+1)
                dfs(pos+1)
                flip(i,j,digit)
                mask &= mask-1

                if valid:
                    return

        ## 按下标对应的位置（下标从0开始对应+1的数），标记该数是否使用
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        dots = list()
        ## 遍历board数独， 将已知的数字，在对应的line， column ， block列表中 
        ## 按下标对应的位置（下标从0开始对应+1的数） 标记为True 
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    dots.append((i,j))
                else:
                    digit = int(board[i][j])-1
                    flip(i,j, digit)
        dfs(0)
