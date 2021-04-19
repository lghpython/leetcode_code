class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # words 单词拼接长度
        sl = len(s)
        count = len(words)
        wl = len(words[0])
        l = count*wl
        res = []
        for i in range(sl-l+1):
            if self.verified(s[i:i+l], list(words),wl):
                res.append(i)
        return res
        
    def verified(self, s, words,wl):
        for i in range(0,len(s)+1,wl):
            if s[i:i+wl] in words:
                words.remove(s[i:i+wl])
            elif s[i:i+wl]:
                return False
        return True
