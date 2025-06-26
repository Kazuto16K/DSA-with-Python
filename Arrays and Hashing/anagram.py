## LeetCode Easy - Concept : Hashing

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for l1 in s:
            if l1 not in hashmap:
                hashmap[l1] = 1
            else:
                hashmap[l1] += 1
        for l2 in t:
            if l2 not in hashmap:
                return False
            else:
                hashmap[l2] -= 1
        flag = 0
        for v in hashmap.values():
            if v != 0:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            return True
        else:
            return False


obj = Solution()
print(obj.isAnagram('hello','olehl'))
        