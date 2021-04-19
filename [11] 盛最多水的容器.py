class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = min(height[l],height[r])*r
        while l<r :
            
            if height[l]>= height[r]:
                r -= 1
            else:
                l += 1
            ans = min(ans, min(height[l],height[r])*(r-l))
        return ans