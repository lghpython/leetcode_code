class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            skey=''.join(sorted(list(strs[i]))) #字符排序
            res.setdefault(skey,[]) 
            res[skey].append(strs[i])   
        return [x for x in res.values()]  
        # return list(res.values())
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            skey=''.join(sorted(list(s))) #字符排序
            res.setdefault(skey,[]) 
            res[skey].append(s) 
            
        return [x for x in res.values()]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())
