class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(ss,ts):
            for i in ss:
                if ss[i] < ts[i]:
                    return False
            return True

        ans = ''
        tsum = {c:0 for c in t}
        ssum = dict(tsum)
        need = [(i,c) for i,c in enumerate(s) if c in t]
        less = len(s)
        sta = 0
        for c in t:
            tsum[c] += 1
        for i,c in need:
            ssum[c] += 1
            while check(ssum,tsum):
                if i-need[sta][0]<less:
                    less = min(less,i-need[sta][0])
                    ans = s[need[sta][0]:i+1]
                ssum[need[sta][1]]-=1
                sta += 1
        return ans

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        ins =[]
        need = []
        for i, c in enumerate(s):
            if c in t:
                ins.append(i)
                need.append(c)
        tsum = {c:0 for c in t}
        ssum = dict(tsum)
        for k in t: tsum[k]+= 1
        left = 0
        less = len(s)
        ans = ''
        for i,n in enumerate(need):
            ssum[n]+=1
            while self.check(ssum,tsum):
                if ins[i] - ins[left] < less:
                    less = ins[i]- ins[left]
                    ans = s[ins[left]:ins[i]+1]
                ssum[need[left]] -= 1
                left += 1
        return ans
    def check(self, ssum, tsum):
        for i in tsum:
            if ssum[i]< tsum[i]:
                return False
        return True
