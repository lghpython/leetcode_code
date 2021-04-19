class Solution:
    def romanToInt(self, s: str) -> int:
        """ 取余法 判断前一位大小"""
        sum = 0
        for i in s:
            if i=='I':
                sum += 1
            elif i=='V':
                sum += 3 if sum%5 == 1 else 5
            elif i=="X":
                sum += 8 if sum%10 == 1 else 10
            elif i=="L":
                sum += 30 if sum%50 == 10 else 50
            elif i=='C':
                sum += 80 if sum%100 == 10 else 100
            elif i=="D":
                sum += 300 if sum%500 == 100 else 500
            elif i=="M":
                sum += 800 if sum%1000 == 100 else 1000
        return sum