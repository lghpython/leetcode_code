class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        prefix = [1]
        digits = '123456789'[:n]
        more = -1 # 记录大于k的前缀位置
        # 保存i个元素组成的字符种类， i的阶乘
        for i in range(2,n+1):
            cur = i*prefix[-1]
            prefix.append(cur)
            if cur>k and more == -1:
                more = i
        # 刚好 k的值为prefix列表， 为该位最大值
        if k in prefix:
            pos = prefix.index(k)
            return digits[:n-pos-1] + digits[n-pos-1:][::-1]
        # 
        pre = prefix[:more-1]
        done = digits[:n-more]
        will = list(digits[n-more:])
        def dfs(k, tmp):
            if not pre: return tmp+''.join(pre)
            d,m = divmod(k,pre.pop())
            if m==0:
                return tmp + will.pop(d-1) + ''.join(will[::-1])
            else:
                return dfs(m, tmp + will.pop(d))

        return dfs(k,done)
        

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        pre = [1]
        digits =['']+[i for i in '123456789'[:n]]
        ans=[]
        for i in range(2,n+1):
            pre.append(i*pre[-1])
        m = 0

        def dfs(k:int,ans):
            if not pre: return 
            d,m = divmod(k,pre.pop())

            if m==k and m<pre[-1]  : 
                ans.append(digits.pop(0))
                dfs(m,ans)
            
            elif m==0:
                ans += [digits.pop(d-1)] + digits[::-1]
            else:
                ans.append(digits.pop(d))
                dfs(m,ans)
            return

        dfs(k,ans)
        return ''.join(ans)

        
        