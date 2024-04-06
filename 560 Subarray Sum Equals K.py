from typing import List
class Solution:
    def subarraySum (self, nums: List[int], k: int) -> int:
        
        length = len(nums)
        returnValue = 0

        #Stores each prefix snapshot
        prefixSum = [0] * length
        currentSum = 0

        #{prefixSum : counter}
        prefixSumHash = {}


        #Loop every value
        #O(n)
        for i in range(length):
            #Add the current value to our prefixSum
            currentSum += nums[i]
            prefixSum[i] = currentSum

            #Save prefixSum and how many times it's appeared 
            if prefixSumHash[i]:
                prefixSumHash[prefixSum[i]] = prefixSumHash[prefixSum[i]] + 1
            else: 
                prefixSumHash[prefixSum[i]] = 1
        return returnValue
    
testing = Solution()

examples = [

    [1, -1, -1, -1, 1], -1,         #Expecting 5  
    #Given examples
    [1 , 1, 1] , 2,     #Expecting 2
    [1, 2, 3], 3,       #Expecting 2

    #Single edge cases
    [10], 10,   #Expecting 1
    [100], 1,   #Expecting 0

    #Doubles edge cases
    [-1, 1], 0,     #Expecting 1
    [1, 1], 1,      #Expecting 2

    #Personal edge cases
     
    [-1, -1, -1, -1, -1, -1], -2,   #Expecting 4
    [1, 1, 1, 1, 1, 1], 3,          #Expecting 3
]

for i in range(0, len(examples), 2):
    print(
        "Array: " + str(examples[i]) + "\tK value: " + str(examples[i+1]) + "\n"
        "Output: " + str(testing.subarraySum(examples[i], examples[i + 1])) + "\n"
    )
"""
Notes:
- We are given a desired value: K
- We add the value of nums every time
- This alue will either: equal K or not equal K
- We can use previous work done to determine how close to K we are
    If: 
        (current work) + (previous work) = k
        returnValue += 1

Tools:
PrefixSum: keeps track of current work
Hashmap: [prefixSum : count] 
    This keep tracks of the previous prefixSums we've encountered
    This will let us know easily let access previous work


Restrictions: 
- guaranteed at least 1 value
- Negatives, zero, positives values for both elements AND K
- Arrays are not expected to be sorted
"""