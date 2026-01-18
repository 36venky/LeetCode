class Solution():
    def productExceptSelf(self,nums:list[int]) -> list[int]:
        n = len(nums)
        lmul = 1                                    # 1[1,2,3,4]1 **Imp**
        rmul = 1
        larr = [0]*n
        rarr = [0]*n

        for i in range(n):
            j = -i-1                                # Used to iterate form both the side simulteneously !!
            larr[i] = lmul
            rarr[j] = rmul
            #print(larr,rarr)
            lmul *= nums[i]
            rmul *= nums[j]
        
        return [l*r for l,r in zip(larr,rarr)]      # Access eles from tow diff list simulteneously !!

x = Solution().productExceptSelf([1,2,3,4])         # Output : [24, 12, 8, 6]
print(x)

# s = [1,2,3,4]
# for i in range(len(s)):
#     j = -i-1
#     print(s[i],s[j])
#
# Output: 1 4
#         2 3
#         3 2
#         4 1