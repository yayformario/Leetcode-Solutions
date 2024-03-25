from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Quick exit
        if len(nums) == 1:
            return 0
        
        #Get the sum 
        totalSum = sum(nums)

        #Left and right sum
        leftSum = 0
        rightSum = 0

        #loop prefixSum
        for left in range(len(nums)):
            #Calculate right sum; 
            #(total - left) is the right sum
            #We can't include our pivot index, so exclude nums[left]
            rightSum = totalSum - leftSum - nums[left]
            #Break condition is leftSum matches rightSum
            if leftSum == rightSum:
                return (left)
            
            #Increment leftSum 
            leftSum += nums[left]
        
        #If we break out the loop, couldn't find anything
        return -1
    
testing = Solution()

examples = [
    #Given examples
    [1,7,3,6,5,6], #Expecting 3
    [1,2,3], #Expeciting -1
    [2,1,-1], #Expecting 0

    #One element examples:
    [10], #All should return 1 (Left and right are zero)
]

for ex in examples:
    print(
        "Input: " + str(ex) + "\n" + 
        "Output: " + str(testing.pivotIndex(ex))
    )

"""
Constraints:
- Leftmost pivot index is the answer
- Left and right edges have sums of zeros
- Guaranteed at least 1 element
- Negative values 
"""