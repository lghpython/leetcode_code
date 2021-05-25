class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums:int, tmp: int):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:],tmp + [nums[i]])
        dfs(nums, [])
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #  itertools 库的全排列方法 permutations
        # print(itertools.permutations(nums))
        import itertools
        return list(itertools.permutations(nums))