class Solution:
    def isNumber(self, s: str) -> bool:
        digits = '0123456789'
        if s[0] in 'eE' or s[-1] in 'eE+-':  
            return False
        # 标记 有效特殊符号出现状态
        has_dot=False
        has_e=False
        has_digit = False
        # 首位或e的下一位是否出现 '+-' 号
        onehassign =False
        ehassign=False
        
        i=0
        while i<len(s):
            if s[i] in '+-':
                if onehassign and not has_e or ehassign or i>0 and s[i-1] not in 'eE':
                    return False
                if i==0:
                    onehassign=True
                if has_e and s[i-1] in 'eE':
                    ehassign = True
            elif s[i] in 'eE':
                if has_e or i==0 or not has_digit: 
                    return False
                else: has_e = True
            elif s[i]=='.' :
                if has_dot or has_e: 
                    return False
                else: has_dot = True
            elif s[i] not in digits:
                return False
            else:
                has_digit = True
            i+=1
         
        return True if has_digit else  False