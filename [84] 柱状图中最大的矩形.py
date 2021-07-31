class Solution:
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