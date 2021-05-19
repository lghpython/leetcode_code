class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ln = len(nums)
        most = 0
        for i in range(ln):
            if i<= most:
                most= max(most, i + nums[i])
            if most>= ln-1:
                return True     
        return False