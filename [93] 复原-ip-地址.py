#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        def dfs(start, step, ip):
            # print(ip, start)
            if ip :
                if ip[-1] == '' or len(ip[-1])>1 and ip[-1][0] == '0' or int(ip[-1])> 255 :
                    return
            if start == n and len(ip) == 4: 
                ans.append('.'.join(ip))
            if  start >=n or len(ip)>=4: return 
            
            for i in [3,2,1]:
                dfs(start+i, i, ip + [s[start: start+i]])
                
        dfs(0,0,[])
        return ans
# @lc code=end

