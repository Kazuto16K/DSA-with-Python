class Solution(object):

    def twoSum(self, numbers, target):
        
        ub = len(numbers)-1
        lb = 0
        while lb < ub:
            if numbers[lb] + numbers[ub] == target:
                return [lb+1,ub+1]
            elif numbers[lb] + numbers[ub] > target:
                ub -= 1
            elif numbers[lb] + numbers[ub] < target:
                lb += 1

obj = Solution()
print(obj.twoSum([-1,0],-1))