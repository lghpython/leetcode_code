class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dlen = len(digits)
        up = False
        for d in range(dlen):
            if digits[-1-d]==9:
                up =True
                digits[-1-d]=0
            else:
                up =False
                digits[-1-d]+=1
                break
        if up:
            return [1] + digits
        return digits
                

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9: 
                digits[i] = 0
            else:
                digits[i] += 1
                break
        if digits[0] == 0: if digits[0] == 0: return [1] + digits
        return digits