class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        twice = False
        pre = 0
        cur = 1
        # 双指针法， twice 标记为出现两次， 统一删除重复的3，4，5，。。 次
        while nums[ cur:]:
            if nums[pre] != nums[cur]:
                twice = False
            elif twice:
                while nums[cur:] and nums[cur] == nums[pre]:
                    nums.pop(cur)
                twice = False
            else :
                twice = True
            pre = cur 
            cur  += 1