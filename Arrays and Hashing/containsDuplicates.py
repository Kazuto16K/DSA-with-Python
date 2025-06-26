## LeetCode Easy

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_map = {}
        for n in nums:
            if n in dict_map:
                dict_map[n] += 1
            else:
                dict_map[n] = 1
        
        for k,v in dict_map.items():
            if v > 1:
                return True
            else:
                continue
        return False
                
obj = Solution()
print(obj.containsDuplicate([1,3,2,1]))