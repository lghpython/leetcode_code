class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """括号生成， 回溯法"""
        ans = []
        def backstack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backstack(S,left+1, right)
                S.pop()
            if left > right:
                S.append(')')
                backstack(S, left, right+1)
                S.pop()
        backstack([], 0, 0)
        return ans