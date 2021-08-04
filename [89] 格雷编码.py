#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        """
        1. 镜像添加高数位， 原理类似前缀和
        2. n总是 n-1 的两倍，除多出的高位1 ，其他数位为 [n-1位置] + (2**(n-1)*[n-1位置镜像])
        """
        res = [0]
        pos = 1
        while pos < 2**n: 
            # res += [pos + i for i in res[::-1]]
            res.extend([pos + i for i in res[::-1]])
            pos<<=1
        return res

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        if n == 0: return res
        def dfs(res,pos):
            if pos == 2**n: return
            # res += [pos + i for i in res[::-1]]
            res.extend([pos + i for i in res[::-1]])
            dfs(res, pos<<1)
        dfs(res,1)       
        return res

# @lc code=end

