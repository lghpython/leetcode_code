class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        prefix = [0] * n
        maxarea = 0 # 当前最大面积
        for i in range(m):
            for j in range(n):
                prefix[j] = prefix[j] + 1  if matrix[i][j]=="1" else 0
            maxarea = max(maxarea, self.largestRectangleArea(prefix))
        return maxarea

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈
        stack = [-1]
        maxarea = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]]> h:
                maxarea = max(maxarea, heights[stack.pop()]*(i - stack[-1] -1 ))
            stack.append(i)
        return maxarea