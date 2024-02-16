class Solution (object):
    def maxSubarraySumCircular(self, nums):
        #---Kadane's Algo Gimmick:
        #Find the global minumum
        #   If circular: (Total) - (Global Min) = maxSum answer

        #===----- For regular maxSum -----===# 
        maxSum = nums[0]
        currentMaxSum = 0
       
        #===----- For circular sum -----===# 
        minSum = nums[0]
        currentMinSum = 0
        totalSum = 0

        #Looping entire list: O(n)
        for n in nums:
            
            #Keep track of current and max sum
            currentMaxSum = max(n, n + currentMaxSum)
            maxSum = max(maxSum, currentMaxSum)

            #Keep track of current and min sum 
            currentMinSum = min(n, n + currentMinSum)
            minSum = min(minSum, currentMinSum)

            #Keep track of total sum
            totalSum += n

        #--- Edge Case: Noncircular largest sum; simply return maxSum ---#
        noncircularSum = maxSum

        #--- Edge Case: Circular largest sum; (Total - minSum) = maxSum
        circularSum = (totalSum - minSum)

        #--- Edge Case: All negative values; simply return maxSum (else return whatever is larger: circular vs noncircular)
        if (maxSum < 0):
            return maxSum
        
        else:
            return max(circularSum, noncircularSum)
        #--- The code above can be summarized as:
        #return (max(noncircular, circular) if (maxSum > 0) else (maxSum))
    

testing = Solution()
examples = [
    #Given examples
    [1,-2,3,-2],
    [5,-3,5],
    [-3,-2,-3]
    
    #Single element examples
    [10],
    [-1],

    #Two element examples
    [2,3],
    [-1,10],
    [-5,3],
    [-2,-4],

    #Three element examples, noncircular
    [1,2,3],
    [-4,-5,-6],
    [-100, 15, -100],

    #Three element examples, circular
    [10,-10,10],
    [10,9,8,-100,0,0,3,0,0,-100,0,1,2]


]
print(testing.maxSubarraySumCircular(examples))