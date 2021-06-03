class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = a.rjust(len(b),'0')
        b = b.rjust(len(a),'0')
        res = ''
        up = False
        for x,y in zip(a[::-1],b[::-1]):
            if not up and x==y or up and x!=y:
                res += '0'
            elif up and x==y or not up and x!=y:
                res += '1' 

            if x ==y =='1' and not up or  x!=y and up:
                 up = True  
            if x ==y =='0' and up or  x!=y and not up:
                 up = False
        return '1' + res[::-1] if up else res[::-1]