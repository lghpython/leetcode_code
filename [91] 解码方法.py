#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:

        # """
        res = [1] + [0]* len(s)
        pre = "0"
        for i,n  in enumerate(s+' '):
            if pre != '0':# 匹配单字符字母
                res[i] += res[i-1]
            if i>1 and s[i-2] != '0' and s[i-2:i]<='26': # 匹配双数字字母
                res[i] += res[i-2]
            pre = n
        return res[-1]
        """ # 官方版
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]
        """
            

# @lc code=end

"1263847121112321212212"