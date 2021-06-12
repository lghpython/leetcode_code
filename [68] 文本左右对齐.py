class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        count = 0 # 长度计数 
        start = 0 # 保存一组起始索引
        for i,word in enumerate(words):
            l = len(word)
            if count + l < maxWidth:
                # 单词之间至少一个空格
                count += l+1
                continue
            elif count+l==maxWidth:
                # 空格数刚好为1 ,起始: start ，终止: i   切片 works[start:i+1]
                res.append(' '.join(words[start:i+1]))
                start = i+1
                count = 0
            else: 
                # i-start 为本组单词数, 起始: start ，终止: i-1 切片 works[start: i]
                space = maxWidth-count+i-start
                if i-start==1: 
                    s = words[start].ljust(maxWidth,' ')
                else:
                    d,m = divmod(space,i-start-1) 
                    # 分割最少 d 个空格， 左边 m 个加1
                    s = (' '*(d+1)).join(words[start:start+m+1])+' '*d+(' '*d).join(words[start+m+1:i])
                res.append(s)
                count=l+1
                start = i
        
        if words[start:]:
            s = ' '.join(words[start:]).ljust(maxWidth," ")
            res.append(s)
        
        return res

