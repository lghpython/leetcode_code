class Solution:
    def countAndSay(self, n: int) -> str:
        """ 递归法 """
        if n==1: return '1'
        return self.explain(self.countAndSay(n-1))

    def explain(self, n):
        res = ''
        tmp,count= 0,0
        for i,s in enumerate(n):
            if tmp and tmp != s:
                res += str(i-count)+tmp
                count = i
            tmp = s

        res += str(len(n)-count)+n[-1]
        return res
        # 正则表达式
        # p = r'(\d)\1*'
        # pattern = re.compile(p)
        # res = [_.group() for _ in pattern.finditer(n)]  # 提取结果
        # return ''.join(str(len(c)) + c[0] for c in res)  