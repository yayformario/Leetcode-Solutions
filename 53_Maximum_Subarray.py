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

            #Check to see if currMax is larger than zero; negative sums don't add anything
            currentSum = max(0, currentSum)
            currentSum += n

            #--- Alternative: We either take (n) on it's own or (n + current)
            #--- Honestly, we usually take (n + current) unless adding current makes it worse than just taking n alone
            #--- currentSum = max(n, n + currentSum)

            #Update max sum if current sum is larger
            maxSum = max(currentSum, maxSum)

        return maxSum
    
testing = Solution()
example = [-1]
print(testing.MaxSubArray(example))