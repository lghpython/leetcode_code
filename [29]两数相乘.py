class Solution:
    def divide(self, dividend: int, divisor: int) -> int: 
        # if divisor == 1: return dividend
        # if divisor == -1:
        #     return -dividend if -dividend < 2147483647 else 2147483647
        dd = abs(dividend)
        dr = abs(divisor)
        
        ans = self.divi(dd,dr)
        if not ((dividend>0) ^ (divisor>0)):
            return ans if ans < 2147483647 else  2147483647
        else:
            return -ans

    def divi(self, d, r):
        if d < r : return 0
        sor = r
        ans = 1
        while d >= sor + sor:
            sor += sor
            ans += ans
        return ans + self.divi(d-sor, r)