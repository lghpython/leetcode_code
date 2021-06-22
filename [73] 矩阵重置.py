class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = '_'
        for raw in matrix:
            if 0 in raw:
                for i in range(len(raw)):
                    if raw[i] ==0 and '_'+str(i)+"_" not in zero:
                        zero += str(i)+"_"
                raw[:] = [0]*len(raw)
        for raw in matrix:
            if raw[0]!=0:
                for z in zero.split('_'):
                    if z:
                        raw[int(z)] = 0



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0
