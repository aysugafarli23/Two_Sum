class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i
            
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in d and i != d[x]:
                return [i, d[x]]
        return None
    
    
    
sol = Solution()
result = sol.twoSum(nums = [1, 8, 9, 5, 16, 2], target = 10)
print(result)