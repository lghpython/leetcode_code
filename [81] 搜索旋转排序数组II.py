"""
[81] 搜索旋转排序数组II - 二分法简单分析实现

解题思路: 二分其实挺简单的只要写出以下步骤

1. while 条件： # 一般 l<=r 进入
2. if 条件： return True # 返回结果
3. elif 条件： l = mid # 用 or 堆砌所有进入右边的条件
4. elif 条件： r = mid # 用 or 堆砌所有进入左边的条件
5. 把所有满足的条件堆上去， 再根据问题添加不同题型的特殊条件就ok
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums)-1
        if r == l: return nums[0] == target
        while l < r:
            mid = l + (r-l)//2
            if target == nums[mid] or target == nums[l] or  target == nums[r]: 
                return True
            
            elif nums[l] < target < nums[mid] or nums[mid] < nums[r] < target:
                
                r = mid  # 在左边 
            elif nums[mid]< target <nums[r] or target < nums[r]<nums[mid]:
                
                l = mid # 在右边
            
            elif nums[mid] == nums[r]:
                r -= 1
            else:
                l += 1
            if r -l < 2: return False
        return False

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            # 同时验证三值
            if target == nums[mid] or target == nums[l] or  target == nums[r]: 
                return True
            elif nums[l] < target < nums[mid] or nums[mid] < nums[r] < target:
                r = mid  # 在左边 
            elif nums[mid]< target <nums[r] or target < nums[r]<nums[mid]:
                l = mid  # 在右边
            # 左中右三值已验证
            r -= 1
            l += 1
        return False
