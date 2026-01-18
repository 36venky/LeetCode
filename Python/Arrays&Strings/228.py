class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        i = 0
        while i < len(nums):
            start = i
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:     # If the num in nums r consecutive , continue !!
                i += 1
            if start == i:                                              # If no consecutive num , append them as it is .
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start]) + "->" + str(nums[i]))      # If consecutive nums exists ,
            i += 1                                                      # append only the first and last num with a "->" in between !!
        return ans

x = Solution().summaryRanges([1,2,4,8,6,5,9])  
print(x)

'''
Sample Usage
ip : [1,2,4,5,6] , Op : ['1->2', '4->6']
ip : [1,2,4,5,6,8,9] , Op : ['1->2', '4->6', '8->9']
ip : [1,2,4,8,6,5,9] , Op : ['1->2', '4', '8', '6', '5', '9']
'''