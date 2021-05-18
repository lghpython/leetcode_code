class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target: return []
        candidates= sorted([c for c in candidates if c<=target])
        clen = len(candidates)
        res = []
        def dfs(i, csum, tmp):
            if i==clen and csum==target and tmp not in res: 
                res.append(tmp)
            if csum > target or i == clen:  return
            if target==csum and tmp not in res:
                res.append(tmp)
                return
            
            dfs(i+1,csum + candidates[i], tmp+[candidates[i]])
             # 以下标i 开始的所有组合回溯完，下标右移 tmp 为 空列表
            dfs(i+1,csum,tmp) 
        # dfs(下标索引，当前总和， 列表保存值 )
        dfs(0,0,[])
        return res