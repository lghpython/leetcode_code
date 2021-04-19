class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        从右往前
        """
        # [1,3,2]
        copy = list(nums)
        l = len(nums)
        for x in range(l-2,-1,-1): # [2,3]
            for y in range(l-1,x,-1):
                if nums[x] < nums[y]:
                    nums[x],nums[y] = nums[y],nums[x]
                    self.sortList(x,nums)
                    break
            if nums != copy: break
        if nums == copy: nums.sort()

    def sortList(self, i , nums):
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1