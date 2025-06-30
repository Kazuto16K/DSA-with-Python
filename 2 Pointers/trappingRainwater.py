class Solution_OrderN_Space(object):  # TC: O(n)
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxLeft = [0]
        maxRight = [0]
        minLR = []
        total_water = 0

        curr_max = 0
        for i in height:
            if i > curr_max:
                curr_max = i
            maxLeft.append(curr_max)

        curr_max = 0
        for i in range(len(height)-1,0,-1):
            if height[i] > curr_max:
                curr_max = height[i]
            maxRight.insert(0,curr_max)
        
        maxLeft = maxLeft[:-1]
        
        for i in range(len(maxLeft)):
            if maxLeft[i] < maxRight[i]:
                minLR.append(maxLeft[i])
            else:
                minLR.append(maxRight[i])

        for i in range(len(height)):
            v = minLR[i] - height[i]
            if v > 0:
                total_water += v
        return total_water
        
obj = Solution_OrderN_Space()
print(obj.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))