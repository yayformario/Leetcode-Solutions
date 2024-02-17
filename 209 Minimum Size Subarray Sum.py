class Solution (object):
    def minSubArrayLen(self, target, nums):
        minLength = len(nums) + 1

        #Two Pointer approach
        leftPointer = 0
        currentSum = 0

    

        for rightPointer in range(len(nums)):
            currentSum += nums[rightPointer]

            while (currentSum >= target):
                #check to see if it's our min length
                minLength = min(minLength, (rightPointer-leftPointer + 1))
                currentSum -= nums[leftPointer]
                leftPointer += 1

        if (minLength == len(nums) + 1):
            return 0 

        return minLength
    
testing = Solution()

examples = [
    #given examples:
    7, [2,3,1,2,4,3], #expecting 2
    1, [1,4,4], #expecting 1
    11 , [1,1,1,1,1,1,1,1], #expecting 0
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