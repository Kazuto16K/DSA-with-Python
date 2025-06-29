"""
LeetCode - Medium
Concept: Sort the array first, Then iterate through the array and use 2 sum II solution

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # sorting the array
        nums.sort()

        #applying 2sum II
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:        ## Not reusing the same value and i>0 means not first index
                continue
            
            l, r = i +  1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res
        
obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))            