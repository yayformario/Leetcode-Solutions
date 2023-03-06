class Solution (object):

    def MaxSubArray (self, nums):

        #--Kadane's Algo
        # Only take into account positive subarrrays
        
        #--Runtime: O(n)
        # We go through every value in the list (length of n)
        
        #--Spacetime: O(1)
        # Only needed three variables to calculate

        #Initialize sums
        currentSum = 0
        maxSum = nums[0] #Edge case: What if list only has negative values?

        #Loop entire array
        for n in nums:

            #Only store positive values, we reset current sum if it's ever negative
            currentSum = max(0, currentSum)

            #Store the next value
            currentSum += n

            #The above code can be simplified to:
            #currentSum = max(n, currentSum + n)

            #Update max sum if current sum is larger
            maxSum = max(currentSum, maxSum)

        return maxSum
    
testing = Solution()
example = [-1]
print(testing.MaxSubArray(example))