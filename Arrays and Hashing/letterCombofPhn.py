class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        #res = []
        if len(digits) == 0:
            return []
            
        res = digit_map[digits[0]]
        for d in range(1,len(digits)):
            digit_vals = digit_map[digits[d]]
            v = len(res)
            res = res*(len(digit_vals))
            for i in range(len(res)):
                res[i] += digit_vals[i//v]


        return res

obj = Solution()
print(obj.letterCombinations("234"))