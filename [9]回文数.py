class Solution:
    def isPalindrome(self, x: int) -> bool:

        n = str(x)
        ln = len(n)
        return n[:ln//2]==n[::-1][:ln//2]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == int(str(abs(x))[::-1])

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        return n==n[::-1]
