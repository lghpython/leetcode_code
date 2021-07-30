class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ 回溯法 """
        res = []
        n = len(nums)
        def dfs(start, tmp):
            
            res.append(tmp[:])
            if start==len(nums): return 
            # 遍历递归输出， 添加一遍所有可能 
            for i in range(start,n):
                tmp.append(nums[i])
                dfs(i+1, tmp)
                tmp.pop()

        dfs(0,[])
        return res