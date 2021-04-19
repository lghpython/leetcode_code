# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。 
# 
#  示例 1: 
# 
#  输入: 123
# 输出: 321
#  
# 
#  示例 2: 
# 
#  输入: -123
# 输出: -321
#  
# 
#  示例 3: 
# 
#  输入: 120
# 输出: 21
#  
# 
#  注意: 
# 
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。 
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        if num[0] == '-':
            result = int(num[1:][::-1]) * -1
        else:
            result = int(num[::-1])
        if result > 2 ** 31 - 1 or result < -2 ** 31:
            return 0
        return result
# leetcode submit region end(Prohibit modification and deletion)
