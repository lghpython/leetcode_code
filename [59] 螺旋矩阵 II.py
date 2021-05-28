class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        t,b,l,r = 0,n,0,n # 上下左右边界
        matrix = [[0 for _ in range(n)] for _a in range(n)]
        i = 1
        while i< n*n:
            # 向右
            for y in range(l,r):
                matrix[t][y] = i
                i+=1
            t+=1
            # 向下
            for x in range(t,b):
                matrix[x][r-1] = i
                i+=1
            r-=1
            # 向左
            for y in range(r-1,l-1,-1):
                matrix[b-1][y] = i
                i+= 1
            b-=1
            # 向上
            for x in range(b-1,t-1,-1):
                matrix[x][l] = i
                i += 1
            l+=1
        else:
            if matrix[t][r-1] == 0 :
                matrix[t][r-1] = i
        return matrix


            