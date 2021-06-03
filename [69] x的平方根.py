class Solution:
    def mySqrt(self, x: int) -> int:
        ''' 二分法 '''
        l,r = 0,x 
        mid = x
        while l != r:
            # print(l,r,mid)
            s = mid*mid
            if s ==x or s < x and (mid+1)*(mid+1) > x  :
                return mid
            elif s > x:
                r = mid
            else:
                l = mid
            mid = (r+l)//2
        return x

class Solution:
    def mySqrt(self, x: int) -> int:
        ''' 二分法 '''
        if x<=1: return x
        r = x
        while r>x//r:
            r = (r + x//r)//2
        return r

