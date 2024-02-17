class Solution (object):
    def minSubArrayLen(self, target, nums):
        #Target of 1 will always return 1
        #Only possible due to constraints
        if (target == 1):
            return 1
        
        #We want to return the SMALLEST possible subarray if it exists
        #(len + 1) takes into account case that entire array sums to target
        #If by the end of loop it's still (len+1), we turn default value 0
        minLength = len(nums) + 1

        #Two Pointer approach
        leftPointer = 0
        currentSum = 0    

        for rightPointer in range(len(nums)):
            currentSum += nums[rightPointer]
            #Window can continue to shrink if given a very large value
            while (currentSum >= target):
                #check to see if it's our min length
                minLength = min(minLength, (rightPointer-leftPointer + 1))
                currentSum -= nums[leftPointer]
                leftPointer += 1

        #Check if we ever found the target
        if (minLength == len(nums) + 1):
            return 0 

        return minLength
    
testing = Solution()

examples = [
    #given examples:
    7, [2,3,1,2,4,3], #expecting 2
    1, [1,4,4], #expecting 1
    11 , [1,1,1,1,1,1,1,1], #expecting 0

    #One element example
    6, [3], #Expecting 0
    5, [4], #Expecting 1

    #Smallest target example; always will be 1
    1, [100,1,2,3,4,5,6,7,8,9,22], #expecting 1

    #Target exceeds sums
    100000, [10000, 10000, 10000], #expecting zero

    #Entire array example
    10, [1,1,1,1,1,1,1,1,1,1] # Expecting 10
]

for i in range(0, len(examples), 2):
    print(
        "target: " + str(examples[i]) + 
        "\tInput: " + str(examples[i+1]) +
        "\nOutput: " + str(testing.minSubArrayLen(examples[i], examples[i+1])) +
        "\n"
    )

"""
Notes:

Constraints:
Target can't be zero
Gauranteed 1 element
No negatives; no zeros (Lowest value an element can be is 1)
"""