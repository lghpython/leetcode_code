class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = sorted(nums)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums[:] = sorted(nums)
        n = len(nums)
        l, r = 0,n-1
        for i in range(0,n):
            while r > 0 and nums[r] == 2 :
                r-=1
            if nums[i] == 2 and i<r:
                nums[r],nums[i] = nums[i],nums[r]
                r -= 1
            if nums[i] == 0:
                nums[l],nums[i]= nums[i],nums[l]
                l += 1
            


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # r,w,b代表 红，白，蓝边界
        r,w = 0,0
        for b in range(len(nums)):
            # b 对应于 n 的索引
            if nums[b] == 0:
                nums[b] = 2
                nums[w] = 1
                nums[r] = 0
                w+=1
                r+=1
            elif nums[b]==1:
                nums[b] = 2
                nums[w] = 1
                w+=1
            else:
                nums[b] = 2