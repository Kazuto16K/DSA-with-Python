## LeetCode Medium without using Division Operator + O(n) time

class Solution1(object):   ## With Div operator
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_ind = -1
        zero_count = 0
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_ind = i
                zero_count += 1
            else:
                prod *= nums[i]

        if zero_ind == -1:        
            for i in range(len(nums)):
                nums[i] = prod/nums[i]
        elif zero_ind != -1 and zero_count ==1:
            for i in range(len(nums)):
                if  i == zero_ind:
                    nums[i] = prod
                else:
                    nums[i] = 0
        else:
            for i in range(len(nums)):
                nums[i] = 0
        return nums

class Solution2(object): # Without div operator with Postfix and prefixx
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 
        postfix = 1
        for i in range(len(nums)-1 , -1, -1):
            res[i] *= postfix
            print(res)
            postfix *= nums[i]
        return res
    
        
    
obj = Solution2()
print(obj.productExceptSelf([1,2,3,4]))