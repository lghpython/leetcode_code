from _typeshed import StrPath


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 分割暴力法
        for w in s.split(" ")[::-1]:
            if w: return len(w)
        return 0 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 循环抛出

        words = s.split(" ")
        while words:
            ans = words.pop()
            if ans: return len(ans)
        return 0

