class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        kinds = [1]
        pre = 0
        # 当 n 等于【1-9】 所有的排序组合
        for i in range(2, n+1): # 输出 kinds = [1,1,2],  pre = 3
            # print(n,i)
            kinds.append(i*kinds[-1])
            if kinds[-1]*i > k:
                pre = i
                break
        print(kinds, pre, n)
        res = '123456789'[:n-pre+1] # n-pre = 7, res = '123456'
        digits = [str(i) for i in range(n-pre,n+1)] # digits = ['7','8','9']
        print(kinds, res, digits)
        def dfs(x:int):
            if x == 1: return digits.pop() 
            d,m = divmod(x,kinds.pop()) # k = 5, d = 2,  m = 1
            print(x,d,m)
            if m == 0:
                return digits.pop(d) + ''.join(digits[::-1])
            return digits.pop(d) + dfs(m)
                # return dfs(pre//i)

        return res+dfs(k)
