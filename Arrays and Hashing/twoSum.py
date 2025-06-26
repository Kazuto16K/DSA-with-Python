# LeetCode Easy, Concept: Hashmap

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]"""

        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            num = target - nums[i]
            if num in d and i != d[num]:
                return [i,d[num]]

obj = Solution()
print(obj.twoSum([2,7,11,15],9))      