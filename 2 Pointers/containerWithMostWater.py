## Leetcode Medium

## Concept : 2 pointers approach... Compare between values and lb and ub and increment/decrement which is smaller respectively

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lb = 0
        ub = len(height) - 1
        max_area = 0
        while lb < ub:
            base = ub - lb
            hgt = min(height[ub],height[lb])
            area = base*hgt
            max_area = max(max_area, area)
            
            if height[lb] <= height[ub]:
                lb += 1
            else:
                ub -= 1
        return max_area

obj = Solution()
print(obj.maxArea(height=[1,8,6,2,5,4,8,3,7]))