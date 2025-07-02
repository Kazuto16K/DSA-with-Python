class Solution_Naive(object): # O(n2) solution
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = []
        i = 0
        j = 1
        if len(temperatures) == 1:
            return [0]
            
        while i < len(temperatures):
            if j < len(temperatures) and temperatures[i] < temperatures[j]:
                res.append(j-i)
                i += 1
                j = i+1
                continue
            elif j >= len(temperatures):
                res.append(0)
                i += 1
                j = i + 1
            else:
                j += 1
        return res
    
class Solution_Optimal(object):  #O(n) using stack
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []  # pair:[temp,index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:  #while stack is not empty and temp is greater than TOS
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res

obj = Solution_Optimal()
print(obj.dailyTemperatures([73,74,75,71,69,72,76,73]))
