class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        nl = len(needle)
        for i,h in enumerate(haystack):
            if h == needle[0] and haystack[i:i+nl] == needle:
                return i
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle : return 0

        ln = len(needle)
        lh = len(haystack)
        
        j = 0
        while j < lh-ln +1:
            if needle == haystack[j:j+ln]:
                return j
            j += 1
        return -1
