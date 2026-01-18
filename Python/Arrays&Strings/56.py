class Solution():
    def mergeIntervals(self,intervals:list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda interval : interval[0])                     # Sort based on first ele in each nested list !!
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:                       # Overlap Condition : if [-1] ele of 1st list is <= [0] ele of 2nd List
                merged.append(interval)
                #print(merged)
            else:
                merged[-1] = [merged[-1][0] , max(merged[-1][1],interval[1])]   # if the OV is true : get [0] form 1st and [-1] form 2nd List to forma merged interval !!
                #print(merged)       
        return merged

x = Solution().mergeIntervals([[1,5],[4,8]])        # Output : [[1, 8]]
print(x)