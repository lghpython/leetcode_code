class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index =1
        for i in range(1,len(nums)):
            if  nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        pre = nums[0]
        while nums[l:]:
            if nums[l] == pre:
                del nums[l]
                continue
            pre = nums[l]
            l += 1
        return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:return 0
        fast = slow = 1
        n = len(nums)
        while fast<n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow