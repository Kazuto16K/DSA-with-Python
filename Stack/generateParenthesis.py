class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add open parenthesis if open < n
        # only add closing parenthesis if closed < open
        # valid iff open == closed == n

        res = []

        def backtrack(openN, closedN, path):
            if openN == closedN == n:
                res.append(path)
                return
            
            if openN < n:
                backtrack(openN + 1, closedN, path + "(")

            if closedN < openN:
                backtrack(openN, closedN + 1, path + ")")

        backtrack(0,0,"")
        return res
    
obj = Solution()
print(obj.generateParenthesis(3))