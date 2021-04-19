# 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和
# 最接近 target （最接近表示两者之差的绝对值最小）。 
# 
#  如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。 
# 
#  请注意，答案不一定是 arr 中的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [4,9,3], target = 10
# 输出：3
# 解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
#  
# 
#  示例 2： 
# 
#  输入：arr = [2,3,5], target = 10
# 输出：5
#  
# 
#  示例 3： 
# 
#  输入：arr = [60864,25176,27249,21296,20204], target = 56803
# 输出：11361
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^4 
#  1 <= arr[i], target <= 10^5 
#  
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        la = len(arr)
        pre, i = 0, 0
        while i < la:
            # i = 0时 满足条件则 所有值大于target//la
            # arr[i]*(la-i)+pre 表示 往后的值等于当前值
            if arr[i] * (la - i) + pre >= target:
                # more = arr[i:] 超过目标value的数组
                avg = (target-pre)//(la-i)
                return avg if (target-pre)%(la-i) <= la // 2 else avg + 1
            pre += arr[i]
            i += 1
        # 能执行到这里说明 所以值小于target//la
        return arr[-1]
# leetcode submit region end(Prohibit modification and deletion)
