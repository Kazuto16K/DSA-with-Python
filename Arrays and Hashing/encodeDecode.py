# LeetCode Medium - Premium Interview Qs

class Solution:

    def encode(self, strs):
        res=""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
        

    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            len_str = int(s[i:j]) #currently j is at #
            res.append(s[j+1: j+1+len_str])
            i = j+1+len_str
        return res       # Removing the last element which is empty str
    
obj = Solution()
st = obj.encode(["EmojiTest 😊","🌟✨🌟✨🌟","🤖👽🤖👽"])
print(obj.decode(st))