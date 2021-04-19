class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        for i in range(ln):
            if nums[i] >= target:
                return i
        return ln
        # for i, num in enumerate(nums):
        #     if target<=num: return i
        # return len(nums)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ 二分法 """
        l,r =0, len(nums)-1
        mid = 0
        if target>nums[-1]: return r+1
        while l<=r:
            mid = (l+r)//2

            if target >nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid -1
            else: return mid
        return l