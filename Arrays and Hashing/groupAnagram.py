## LeetCode Medium: Concept - Sort strings and Apply Hashmap

##     KEY      ##      VALUE      ###
#    sorted_str  ##     actual_str  ##
#      "aet"      ##    "eat" "tea" "ate" ##

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [strs]
        else:
            dictmap = {}
            for s in strs:
                sorted_chars = sorted(s)
                sorted_str = "".join(sorted_chars)
                if sorted_str not in dictmap:
                    dictmap[sorted_str] = [s]
                else:
                    dictmap[sorted_str].append(s)
            
            ret_list = []
            for v in dictmap.values():
                ret_list.append(v)
            
            return ret_list

obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))            




        