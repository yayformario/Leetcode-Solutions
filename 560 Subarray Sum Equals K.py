<<<<<<< Updated upstream
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return 0
    

=======
from typing import List
class Solution:
    def subarraySum (self, nums: List[int], k: int) -> int:
        length = len(nums)

        if length == 1:
            return 1
        
        returnValue = 0

        prefixSum = [0] * length

        #{prefixSum : counter}
        prefixSumHash = {}

        #Loop every value
        #O(n)
        for i in range(length):
            #Add the current value to our prefixSum
            prefixSum += nums[i]
            prefixSum[i] = prefixSum

        return returnValue
    
testing = Solution()

examples = [
    #Given examples
    [1,1,1] , 2, #Expecting 2
    [1,2,3], 3, #Expecting 3

    #Single edge cases
    [10], 10 #Expecting 1
    [100]
]

    
"""
Notes:
- We are given a desired value: K
- We add the value of nums every time
- This value will either: equal K or not equal K
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
>>>>>>> Stashed changes
