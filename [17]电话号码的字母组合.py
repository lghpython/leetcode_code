class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = len(digits)
        if l==0: return []
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        cur = ''
        def dfs(index,digit,cur ):
            # 出口
            if index == len(digit): 
                ans.append(cur)
                return
            d = digit[index]
            ll = len(dic[d])
            for i in range(ll):
                cur+=dic[d][i]
                dfs(index+1,digit,cur)
                cur=cur[:-1]
        
        dfs(0,digits,cur)
        return ans