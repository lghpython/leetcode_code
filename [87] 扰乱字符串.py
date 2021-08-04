#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        """递归法， 超时 加@cache 缓存"""
        """
        if s1 == s2:return True
        if sorted(s1) != sorted(s2): return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]) :
                return True
            if self.isScramble(s1[-i:],s2[:i]) and self.isScramble(s1[:-i],s2[i:]):
                return True
        return False
        """"
        
# @lc code=end

