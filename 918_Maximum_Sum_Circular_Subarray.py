class Solution (object):
    
    

    
    def maxSubarraySumCircular(self, nums):
        #---Kadane's Algo Gimmick:
        #Find the global minumum
        #   If circular: (Total) - (Global Min) = maxSum answer
    
        #Initialize currMin and currMax
        currMin = 0
        currMax = 0

        #Initialize minSum and maxSum
        minSum = nums[0]
        maxSum = nums[0]

        #intialize total
        total = 0

        #Looping entire list: O(n)
        for n in nums:
            
            #Keep track of current and max sum
            currMax = max(n, n + currMax)
            maxSum = max(maxSum, currMax)

            #Keep track of current and min sum 
            currMin = min(n, n + currMin)
            minSum = min(minSum, currMin)

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