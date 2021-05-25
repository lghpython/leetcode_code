class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums:List, tmp:List):
            if not nums and tmp in res:
                res.append(tmp)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],tmp+[nums[i]])
        dfs(nums,[])
        return res