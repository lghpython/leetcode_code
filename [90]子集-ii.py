#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        def dfs(pos,need, tmp):
            if need == 0: 
                if tmp not in ans:  ans.append(tmp)
                if pos == 0 : 
                    for j in range(1,n+1):
                        dfs(pos,j,tmp) 
            for i in range(pos,n):
                dfs(i+1, need-1, tmp + [nums[i]]) 

        dfs(0,0,[])
        return ans

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        def dfs(pos,need, tmp):
            if need == 0: 
                if tmp not in ans:  ans.append(tmp)
                return
            for i in range(pos,n):
                dfs(i+1, need-1, tmp + [nums[i]]) 

        for j in range(n+1):      
            dfs(0,j,[])
        return ans
# @lc code=end

