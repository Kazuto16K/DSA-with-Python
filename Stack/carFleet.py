# Leetcode 853 (Medium)

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [[p, s] for p, s in zip(position, speed)] #creating an array of pairs

        stack = []
        for p, s in sorted(pair)[::-1]:  # reverse Sorted Order
            stack.append((target - p) / s)

            # if there are 2 cars in stack/road and
            # first car is slower than second car then
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # removing the 2nd car as they become a fleet and thus 1 car kinda combined'

        return len(stack)
            
obj = Solution()
print(obj.carFleet(10, [6,8],[3,2]))