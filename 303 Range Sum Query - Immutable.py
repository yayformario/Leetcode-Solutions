from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        #Create a running prefixSum with an extra slot
        #This is to prevent edge cases
        self.prefixSum = [0] * (len(nums)+1)
        sum = 0

        #O(n)
        for i in range(1, len(nums)+1, 1):
            sum += nums[i-1]
            self.prefixSum[i] += sum

    def sumRange(self, left: int, right: int) -> int:
        
        #offset the indicies for easier calculation
        left = left + 1
        right = right + 1
        return (self.prefixSum[right] - (self.prefixSum[left-1]))

#Given example:
exampleArray = [-2, 0, 3, -5, 2, -1]
exampleRanges = [
    [0, 2], #Expecting 1 
    [2, 5], #Expecting -1
    [0, 5] #Expecting -3
]

testing = NumArray(exampleArray)
for ex in exampleRanges:
    print (
        "Input: " + str(ex) + "\n" + 
        "Output: " + str(testing.sumRange(ex[0], ex[1]))
    )


"""
Gauranteed at least 1 element
Take into account negative numbers
left and right sumRange provided is always in bounds
"""