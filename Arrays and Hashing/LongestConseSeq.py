class Solution_Sort(object):         ## Easy solution TC: O(nlogn)   SC:O(1)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 0:
            return 0
        count = 1
        max_count = 1
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                continue
            elif nums[i-1] + 1 == nums[i]:
                count += 1
            else:
                max_count = max(max_count,count)
                count = 1
            
            max_count = max(max_count,count)

        return max_count 

class Solution_Set(object):    ## Optimal Solution TC: O(n), SC: O(n)   Leetcode medium (128)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        for n in numSet:
            #check if it is start of seq
            if (n-1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest,length)
        return longest