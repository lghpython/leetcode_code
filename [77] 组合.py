class Solution:
    def combine(self, n, k):
        res = []
        # 思路1 [1,...,n] 的列表剔除值每次剔除 一个值 ，当列表长度为k 添加到结果到列表
        # 思路2 [1,...,k] 从k开始一个一个挪
        def dfs(tmp, i):
            # 切片剔除当前值
            nonlocal res
            if len(tmp) == k:
                if tmp not in res:
                    res.append(tmp)
                return
            # 依次删除
            for i in range(n):
                # 索引大于tmp长度删除
                if i>=len(tmp) or len(tmp[:i]) > k: break
                dfs(tmp[:i]+ tmp[i+1:], i)
                
            return
        res = []
        all = [x for x in range(1,n+1)]
        dfs(all,0)
        return res

class Solution2:
    def combine(self, n, k):
        res = []

        def  (start, need, tmp):
            print(start,n-start+1, need)
            if n-start+1 < need: return # 剩余值不足
            if need == 0: 
                res.append(list(tmp))
                return
            for i in range(start,n+1):
                # print(tmp)
                tmp.append(i)
                dfs(i+1,need-1,tmp)
                tmp.pop()
        dfs(1,k,[])
        return res


if __name__ == '__main__':
    solution = Solution()
    print('结果', solution.combine(4,2))

    solution2 = Solution2()
    print('结果', solution.combine(4,2))


  