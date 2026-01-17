def maxProfit(nums):
    l = 0
    h = 0
    profit = 0

    for i in range(len(nums)):
        if nums[i] > nums[i-1]:
            l = nums[i-1]
        elif nums[i] < nums[i-1]:
            h = nums[i]
        
