class Solution:
    def twoSum(self, nums, target):
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i              # Store all nums ele as Key and its index as Value

        for i in range(len(nums)):
            y = target - nums[i]
            if y in h and h[y] != i:    # Both i and y should not hold the same * num * 
                return [i, h[y]]        # Return the list of indeces of current ele and the index of difference !!
            
x = Solution()
print(x.twoSum([2,7,5,3],8))