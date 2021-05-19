class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        presum = [0]
        ans = nums[0]
        for n in nums:
            s = presum[-1]+n
            ans = max(s-min(presum), ans)
            presum.append(s) 
        return ans
            

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """动态规划"""
        pre = 0
        ans = nums[0]
        for n in nums:
            pre = max(pre + n,n)
            ans = max(ans,pre)
        return ans
