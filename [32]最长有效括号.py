# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        最长有效括号子串
        :param s: 输入包含"(" ")" 字符串
        :return: 返回子串长度
        """

        # 1. 出现"(" 开始计数
        # 2. "(" ")" 数量一致 保存组合数量
        # 3. 往后第一个为 ")"
        # 4 往后第一个为"("

        ## 栈
        stack, count = [-1], 0
        for i in range(len(s)):
            if len(stack) - 1 and s[i] == ')' and s[stack.pop()] == '(':
                count = max(count, i - stack[-1])
            else:
                stack.append(i)
        return count

        ## 动态规划

        # ## 替换字符法
        # for i in range(len(s)//2):
        #     s = s.replace('('+'2'*i+')','2'*(i+1))
        # s= s.replace("(", ")")
        # res = [len(c) for c in s.split(')') if c]
        # return 2 * max(res) if res else 0


# leetcode submit region end(Prohibit modification and deletion)
