
class Solution:
    def jump(self, nums: List[int]) -> int:
        ln = len(nums)
        maxi = [i+n for i,n in enumerate(nums)]
        steps, most = 0, 0
        while most < ln-1:
            most  = max(maxi[:most+1]) # 最大步长的位置
            steps += 1
        return steps