class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates= sorted([c for c in candidates if c<=target])
        clen = len(candidates)
        res = []
        def dfs(i, csum, tmp):
            
            if csum > target or i == clen:
                return
            if target==csum:
                res.append(tmp)
                return
            
            dfs(i,csum + candidates[i], tmp+[candidates[i]])
             # 以下标i 开始的所有组合回溯完，下标右移 tmp 为 空列表
            dfs(i+1,csum,tmp)
        # dfs(下标索引，当前总和， 列表保存值 )
        dfs(0,0,[])
        return res