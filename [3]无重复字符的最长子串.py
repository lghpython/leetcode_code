# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = len(s)
        if ls <= 1: return ls
        tmp = []
        l, max, count = 0, 0, 0
        for i in range(ls):
            # 当无重复,添加到列表,max加1
            if s[i] not in tmp:
                tmp.append(s[i])
                count += 1
            else:
                # 出现重复删除第一个,直到不重复
                while s[i] in tmp:
                    tmp.pop(0)
                    l += 1
                    count -= 1
                tmp.append(s[i])
                count += 1
            if count > max:
                max = count
        return max
# leetcode submit region end(Prohibit modification and deletion)
