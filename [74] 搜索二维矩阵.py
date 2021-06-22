class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for li in matrix:
            if li[0]<=target<=li[-1]:
                return target in li
        return False



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """合并一维数组"""
        return target in (reduce(lambda x,y:x+y,matrix))


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ 二分法 """
        l,r = 0,len(matrix)-1
        mid = (l+r)//2
        while l<=r and matrix[0][0] <= target <= matrix[-1][-1]:
            if  matrix[mid][0]<=target<=matrix[mid][-1]:
                return target in matrix[mid]
            elif  matrix[mid][0]>target:
                r = mid-1
            elif matrix[mid][-1]<target:
                l =mid+1
            mid = (l+r)//2
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """二分法"""
        n = len(matrix[0])
        l,r = 0,len(matrix)*n-1
        mid = (l+r)//2
        if not (matrix[0][0] <= target <= matrix[-1][-1]):
            return False
        while l<=r:
            if  matrix[mid//n][mid%n]==target:
                return True
            elif  matrix[mid//n][mid%n]>target:
                r = mid-1
            else:
                l =mid+1
            mid = (l+r)//2
        return False
