class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 上下翻转
        for i in range((n+1)//2):
            matrix[i],matrix[n-1-i] = matrix[n-1-i],matrix[i]
        # 对角翻转
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix[:] = [[matrix[x][y] for x in range(n-1,-1,-1)] for y in range(n)]
