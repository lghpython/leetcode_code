class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ## queries 类别存储了 需要异或计算的 下标边界
        ## 遍历法， 超出时间限制
        res = []
        index = 0
        for l,r in queries:
            # print(index, l)
            res.append(arr[l])
            while l<r:
                res[index] ^= arr[l+1]
                l += 1
            index += 1
        return res


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ## 前缀异或法， 将每次的异或的结果保存到列表
        xors = [0]
        for a in arr:
            xors.append(xors[-1] ^ a)

        # ans = list()
        # for l , r in queries:
        #     ans.append(xors[l] ^ xors[r+1])
        # return ans        
        return  [xors[l]^xors[r+1] for l , r in queries]