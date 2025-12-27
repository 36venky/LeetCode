class Solution:
    def containsDuplicates(self, nums: list[int]) -> bool:
        hash = dict()
        if len(nums) <= 1:
            return False
        for num in nums:
            if num in hash:
                return True
            hash[num] = 1
        return False
    
# x = Solution()
# print(x.containsDuplicates([1,2,3,4]))
# https://leetcode.com/problems/contains-duplicate/description/