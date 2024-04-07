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

        #Not immediately obvious but we will need a way to count the original "zero" for 1 elmeent edge cases
        #Edge case: nums = [3], k = 3
        #Desired value: 3 - 3 = 0 
        #We can always subtract nothing from anything
        #So we need to setup a default key-value pair: { 0 : 1 } 
        prefixSumHash[0] = 1

        #Loop every value
        #O(n)
        for i in range(length):
            #Add the current value to our prefixSum
            currentSum += nums[i]
            prefixSum[i] = currentSum

            #Save prefixSum and how many times it's appeared 
            if prefixSum[i] in prefixSumHash:
                prefixSumHash[prefixSum[i]] = prefixSumHash[prefixSum[i]] + 1
            
            else:
                prefixSumHash[prefixSum[i]] = 1

            #Calculate the value we're looking for
            desiredValue = currentSum - k

            #Check to see if this desiredValue is in our Hash
            if desiredValue in prefixSumHash:
                #By how many times we've encountered the desired value
                #We can also safely pop the key
                returnValue += prefixSumHash.pop(desiredValue)

        return returnValue
    
testing = Solution()

examples = [
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
    [1, -1, -1, -1, 1], -1,         #Expecting 6
    [-1, -1, -1, -1, -1, -1], -2,   #Expecting 5
    [1, 1, 1, 1, 1, 1], 3,          #Expecting 4

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