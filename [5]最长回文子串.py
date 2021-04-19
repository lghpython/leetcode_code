# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        if lens <= 1: return s
        max = ''
        for i in range(lens):
            for j in range(lens - 1, i, -1):
                if s[i] == s[j] and j - i + 1 > len(max) and s[i:j + 1] == s[i:j + 1][::-1]:
                    max = s[i:j + 1]
        if len(max) == 0:
            return s[0]
        return max

        '''
        lens = len(s)
        if len(s) <= 1:
            return s
        start = end = 0
        for n in range(lens):
            l = r = n
            while l >= 0 and r < lens and s[l] == s[r]:
                    l -= 1
                    r += 1
            odd_len = r-l-1
            l = n
            r = n+1
            while l >= 0 and r < lens and s[l] == s[r]:
                    l -= 1
                    r += 1
            even_len = r-l-1
            more_len = odd_len if even_len < odd_len else even_len
            if more_len > end - start+1:
                start = n - (more_len-1)//2
                end = n + more_len//2

        return s[start:end+1]'''
# leetcode submit region end(Prohibit modification and deletion)
