class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # print(nums)
        # for i, num in enumerate(nums):
        #     if num == target:
        #         return i
        # return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
       

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分法：
        
        l, r = 0, len(nums)-1
        while l+1<r:
            mid = (l+r)//2
            # print(mid)
            if nums[mid]>target:
                if nums[r] < nums[mid] and target <= nums[r]:
                    l = mid
                else:
                    r = mid
            elif nums[mid]<target:
                if nums[r]>nums[mid] and target> nums[r]:
                    r = mid
                else:
                    l = mid
            else:
                return mid
        if nums[l] == target: return l
        if nums[r] == target: return r
        return -1