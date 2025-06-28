## LeetCode Medium - Concept hashmap

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        
        ret_list = []

        while k!=0:
            max_v = 0
            max_k = 0
            for key,value in hashmap.items():
                if value >= max_v:
                    max_v = value
                    max_i = key
            hashmap[max_i] = 0
            ret_list.append(max_i)
            k -= 1

        return ret_list
        