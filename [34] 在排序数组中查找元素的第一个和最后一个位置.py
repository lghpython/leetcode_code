class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ 遍历法"""
        start,end = -1, -1
        for i, num in enumerate(nums):
            if start == -1 and num == target:
                start = i
            elif start != -1 and num != target:
                end = i-1
                break
        if start != -1 and end ==-1:
            end = len(nums)-1
        return [start, end]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """二分法， 找到任意一个target值， 再朝两边查找"""
        start,end = -1, -1
        loc =  -1
        l,r = 0, len(nums) -1
        if target not in nums: return [-1, -1]
        while l <= r:
            if nums[l] == target : 
                loc = l
                break
            if nums[r] == target:
                loc = r
                break

            mid = (l+r)//2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                loc = mid
                break
        if loc != -1: 
            pre = nex = loc
            while pre >= 0:
                if nums[pre] == target:
                    start = pre 
                    pre -= 1
                else: break
            while nex <= len(nums)-1:
                if nums[nex] == target:
                    end = nex
                    nex += 1
                else: break
            
        return [start, end]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """列表index 索引查询， 再向右查找"""
        start = end = -1
        loc =  -1
        if target not in nums: 
            return [-1, -1]
        else:
            start = nums.index(target)
        if start != -1: 
            nex = start
            while nex <= len(nums)-1:
                if nums[nex] == target:
                    end = nex
                    nex += 1
                else: break
            
        return [start, end]