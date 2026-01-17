class Solution ():
    def closestNum(self,nums)->int:
        closest = nums[0]

        for x in nums:
            if abs(closest) > x:
                closest = x

        if closest < 0 and abs(closest) in nums:    # Negative nums r allowed !!
            return abs(closest)
        else:
            return closest

x = Solution().closestNum([-2,-1,1,2])
print(x)