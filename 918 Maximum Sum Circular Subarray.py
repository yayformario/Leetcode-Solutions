class Solution (object):
    def maxSubarraySumCircular(self, nums):
        #---Kadane's Algo Gimmick:
        #Find the global minumum
        #   If circular: (Total) - (Global Min) = maxSum answer
    
        #Initialize currMax and currMin
        currentMax = 0
        currentMin = 0

        #Initialize maxSum and minSum 
        maxSum = nums[0]
        minSum = nums[0]
        
        #intialize total
        total = 0

        #Looping entire list: O(n)
        for n in nums:
            
            #Keep track of current and max sum
            currentMax = max(n, n + currentMax)
            maxSum = max(maxSum, currentMax)

            #Keep track of current and min sum 
            currentMin = min(n, n + currentMin)
            minSum = min(minSum, currentMin)

            #Keep track of total sum
            total += n

        #--- Edge Case: Noncircular largest sum; simply return maxSum ---#
        noncircular = maxSum

        #--- Edge Case: Circular largest sum; (Total - minSum) = maxSum
        circular = (total - minSum)

        #--- Edge Case: All negative values; simply return maxSum (else return whatever is larger: circular vs noncircular)
        if (maxSum < 0):
            return maxSum
        
        else:
            return max(circular, noncircular)
        #--- The code above can be summarized as:
        #return (max(noncircular, circular) if (maxSum > 0) else (maxSum))
    

testing = Solution()
example = [0]
print(testing.maxSubarraySumCircular(example))