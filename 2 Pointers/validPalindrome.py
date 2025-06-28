### LEETCODE EASY

class Solution_strRev(object):            ## Reversal of string
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 = s1 + i.lower()
        return s1 == s1[::-1]

class Solution_2pointer(object):                    ### Most Logical Way - 2pointer Method
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z')
        or ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1

        while l < r:
            # make sure both at left and right is alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        

obj = Solution_2pointer()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
